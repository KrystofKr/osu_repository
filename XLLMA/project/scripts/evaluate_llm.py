"""Evaluate two-level predictions against generator scenarios and heuristic labels."""
import argparse
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path

from llm_utils import ID, INPUT_FIELDS, read_csv, load_journal, write_json
from data_paths import DATA, data_path

PREDICTION_FIELDS = [
    ID, 'Zdroj', *INPUT_FIELDS,
    'Kod kategorie LLM', 'Kategorie LLM',
    'Kod hlavni kategorie LLM', 'Hlavni kategorie LLM',
    'Kod scenare', 'Kategorie scenare',
    'Kod hlavni kategorie scenare', 'Hlavni kategorie scenare',
    'Shoda kategorie', 'Shoda hlavni kategorie', 'Konzistentni hierarchie',
    'Kod heuristiky', 'Kod hlavni kategorie heuristiky',
]


def scores(pairs):
    support = Counter(gold for gold, pred in pairs)
    predicted = Counter(pred for gold, pred in pairs)
    correct = Counter(gold for gold, pred in pairs if gold == pred)
    classes = sorted(set(support) | set(predicted))
    per_class = []
    for code in classes:
        precision = correct[code]/predicted[code] if predicted[code] else 0
        recall = correct[code]/support[code] if support[code] else 0
        f1 = 2*precision*recall/(precision+recall) if precision+recall else 0
        per_class.append({'code':code,'support':support[code],'predicted':predicted[code],
                          'precision':precision,'recall':recall,'f1':f1})
    active = [r for r in per_class if r['support']]
    n = len(pairs)
    return {'count':n, 'accuracy':sum(correct.values())/n if n else None,
            'macro_f1':sum(r['f1'] for r in active)/len(active) if active else None,
            'weighted_f1':sum(r['f1']*r['support'] for r in active)/n if n else None,
            'macro_classes':'Only categories with positive target support', 'per_class':per_class}


def write_csv(path, rows, fields):
    temporary = path.with_suffix('.tmp')
    with temporary.open('w',encoding='utf-8',newline='') as handle:
        writer=csv.DictWriter(handle,fieldnames=fields,delimiter=';');writer.writeheader();writer.writerows(rows)
    temporary.replace(path)


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--experiment',type=Path,default=DATA/'experiments/qwen3.5_4b_all_categories')
    parser.add_argument('--allow-partial',action='store_true')
    parser.add_argument('--plots',action='store_true',help='Vytvoří PNG grafy; vyžaduje matplotlib a numpy.')
    args=parser.parse_args(argv);output=args.experiment.resolve()
    if (DATA/'experiments').resolve() not in output.parents:
        parser.error('Experiment musí být pod data/experiments.')
    predictions=load_journal(output/'predictions.jsonl')
    manifest=json.loads((output/'run.json').read_text())
    if manifest['configuration'].get('taxonomy_mode') == 'model_proposed':
        raise ValueError('Vlastní taxonomie má odlišné kódy; použij evaluate_discovered.py.')
    for name,digest in manifest['configuration']['input_hashes'].items():
        if hashlib.sha256(data_path(name).read_bytes()).hexdigest()!=digest:
            raise ValueError('Vstupy se od klasifikace změnily: '+name)
    transactions=read_csv(data_path('data_combined.csv'))
    dictionary={r['Kod kategorie']:r for r in read_csv(data_path('category_dictionary.csv'))}
    groups={r['Kod hlavni kategorie']:r['Hlavni kategorie'] for r in read_csv(data_path('main_category_dictionary.csv'))}
    mapping={r['Puvodni kategorie']:r for r in read_csv(data_path('category_mapping.csv'))}
    scenario_rows=read_csv(data_path('reference_scenarios.csv'))+read_csv(data_path('synthetic_profiles.csv'))
    scenarios={r[ID]:r for r in scenario_rows}
    if len(scenarios)!=len(scenario_rows) or set(scenarios)!={r[ID] for r in transactions}:
        raise ValueError('Scénáře nemají jednoznačné pokrytí všech transakcí.')
    if set(predictions)-set(scenarios):
        raise ValueError('Cizí transakce v predikcích.')
    if not args.allow_partial and len(predictions)!=len(transactions):
        raise ValueError(f'Neúplný běh: {len(predictions)}/{len(transactions)}; dokonči klasifikaci.')
    heuristic={r[ID]:r for r in read_csv(data_path('original_profiles.csv'))}
    enriched=[]
    for transaction in transactions:
        identity=transaction[ID]
        if identity not in predictions:continue
        pred=predictions[identity];gold=mapping[scenarios[identity]['Kategorie']]
        fine=pred['Kod kategorie LLM'];main=pred['Kod hlavni kategorie LLM']
        if fine not in dictionary or main not in groups:raise ValueError('Neplatný výstupní kód.')
        baseline=mapping[heuristic[identity]['Kategorie']] if identity in heuristic else None
        enriched.append({ID:identity,'Zdroj':'reference' if identity.startswith('REF-') else 'synthetic',
                         **{field:transaction[field] for field in INPUT_FIELDS},
                         'Kod kategorie LLM':fine,'Kategorie LLM':dictionary[fine]['Kategorie'],
                         'Kod hlavni kategorie LLM':main,'Hlavni kategorie LLM':groups[main],
                         'Kod scenare':gold['Kod kategorie'],'Kategorie scenare':gold['Kategorie'],
                         'Kod hlavni kategorie scenare':gold['Kod hlavni kategorie'],
                         'Hlavni kategorie scenare':gold['Hlavni kategorie'],
                         'Shoda kategorie':int(fine==gold['Kod kategorie']),
                         'Shoda hlavni kategorie':int(main==gold['Kod hlavni kategorie']),
                         'Konzistentni hierarchie':int(main==dictionary[fine]['Kod hlavni kategorie']),
                         'Kod heuristiky':baseline['Kod kategorie'] if baseline else '',
                         'Kod hlavni kategorie heuristiky':baseline['Kod hlavni kategorie'] if baseline else ''})
    subsets={'all':enriched,'reference':[r for r in enriched if r['Zdroj']=='reference'],
             'synthetic':[r for r in enriched if r['Zdroj']=='synthetic']}
    context = manifest.get('evaluation_context', {})
    pilot_ids = set(context.get('prompt_development_ids', []))
    if pilot_ids:
        subsets['excluding_pilot']=[r for r in enriched if r[ID] not in pilot_ids]
    metrics={'total_transactions':len(transactions),'evaluated':len(enriched),'complete':len(enriched)==len(transactions),
             'target':'Generator scenarios; no independently annotated real-world ground truth',
             'sources':{},'heuristic_agreement':{},
             'prompt_development_overlap':len(pilot_ids & {r[ID] for r in enriched})}
    all_class_metrics=[];confusions=[]
    unknown_code = next(code for code,row in dictionary.items() if row['Kategorie']=='neurčeno')
    for source,rows in subsets.items():
        metrics['sources'][source]={'fine':scores([(r['Kod scenare'],r['Kod kategorie LLM']) for r in rows]),
                                    'main':scores([(r['Kod hlavni kategorie scenare'],r['Kod hlavni kategorie LLM']) for r in rows]),
                                    'both_accuracy':sum(r['Shoda kategorie'] and r['Shoda hlavni kategorie'] for r in rows)/len(rows) if rows else None,
                                    'hierarchy_consistency':sum(r['Konzistentni hierarchie'] for r in rows)/len(rows) if rows else None,
                                    'unknown_rate':sum(r['Kod kategorie LLM']==unknown_code for r in rows)/len(rows) if rows else None,
                                    'fine_wrong_main_correct':sum(not r['Shoda kategorie'] and r['Shoda hlavni kategorie'] for r in rows),
                                    'main_wrong':sum(not r['Shoda hlavni kategorie'] for r in rows)}
        for level in ['fine','main']:
            for record in metrics['sources'][source][level]['per_class']:
                name=dictionary[record['code']]['Kategorie'] if level=='fine' else groups[record['code']]
                all_class_metrics.append({'source':source,'level':level,'name':name,**record})
        for level,target,pred_col in [('fine','Kod scenare','Kod kategorie LLM'),('main','Kod hlavni kategorie scenare','Kod hlavni kategorie LLM')]:
            for (gold,pred),count in Counter((r[target],r[pred_col]) for r in rows).most_common():
                confusions.append({'source':source,'level':level,'target':gold,'prediction':pred,'count':count})
    for level,target,pred_col in [('fine','Kod heuristiky','Kod kategorie LLM'),('main','Kod hlavni kategorie heuristiky','Kod hlavni kategorie LLM')]:
        metrics['heuristic_agreement'][level]=scores([(r[target],r[pred_col]) for r in subsets['reference']])
    write_json(output/'evaluation.json',metrics)
    write_csv(output/'predictions.csv',enriched,PREDICTION_FIELDS)
    write_csv(output/'category_metrics.csv',all_class_metrics,['source','level','name','code','support','predicted','precision','recall','f1'])
    write_csv(output/'confusions.csv',confusions,['source','level','target','prediction','count'])
    def pct(value):return f'{100*value:.2f} %' if value is not None else '—'
    configuration = manifest['configuration']
    options = configuration['options']
    model = configuration['model']
    seconds = manifest.get('wall_seconds', 0)
    completed = manifest.get('completed', 0)
    parameters = [
        ('Model', f'`{model}`'),
        ('Digest modelu', f'`{configuration["digest"]}`'),
        ('Ollama', manifest.get('ollama_version', '—')),
        ('Transakce ve vstupu', len(transactions)),
        ('Kategorie / hlavní skupiny', f'{len(dictionary)} / {len(groups)}'),
        ('Transakce na požadavek', configuration['batch_size']),
        ('Souběžné požadavky při posledním spuštění', manifest.get('last_execution', {}).get('workers', '—')),
        ('Temperature', options['temperature']),
        ('Seed', options['seed']),
        ('Kontext (tokeny)', options['num_ctx']),
        ('Limit odpovědi pro plnou dávku (tokeny)', options['num_predict']),
        ('Thinking', 'zapnuto' if configuration['think'] else 'vypnuto'),
        ('Zaznamenaný čas klasifikace', f'{seconds:.2f} s ({seconds / 60:.2f} min)'),
        ('Průměrný čas na uloženou transakci', f'{seconds / completed:.3f} s' if completed else '—'),
        ('Požadavky na klasifikaci', manifest.get('requests', '—')),
        ('Zpracování neúspěšných odpovědí / dělení dávek', manifest.get('fallback_splits', '—')),
    ]
    lines=[f'# Vyhodnocení {model}','',f'Vyhodnoceno {len(enriched)} z {len(transactions)} transakcí.',
           '', 'Cíl hodnocení: shoda se scénářovou kategorií generátoru. Nejde o ručně ověřenou přesnost na skutečných bankovních datech.',
           '', '## Parametry experimentu', '', '| Parametr | Hodnota |', '|---|---|']
    lines.extend(f'| {name} | {value} |' for name, value in parameters)
    lines.extend(['', 'Čas pochází z run.json a sčítá aktivní spuštění klasifikátoru, včetně požadavků a zápisu výsledků; nezahrnuje pauzy mezi spuštěními ani toto vyhodnocení.',
                  'Limit odpovědi je společný pro celý požadavek. Neúplné odpovědi klasifikátor odmítá.',
                  '', '## Výsledky', '',
                  '| Sada | Počet | Přesnost kategorie | Macro-F1 kategorie | Přesnost hlavní | Macro-F1 hlavní |',
                  '|---|---:|---:|---:|---:|---:|'])
    for source,values in metrics['sources'].items():
        lines.append(f'| {source} | {values["fine"]["count"]} | {pct(values["fine"]["accuracy"])} | {pct(values["fine"]["macro_f1"])} | {pct(values["main"]["accuracy"])} | {pct(values["main"]["macro_f1"])} |')
    lines.extend(['','Macro-F1 průměruje jen kategorie přítomné v cílových datech. Četné kategorie tedy nepřeváží vzácné.',
                  f'Konzistence hlavní a podrobné kategorie: {pct(metrics["sources"]["all"]["hierarchy_consistency"])}.',
                  f'Současně správná obě zařazení: {pct(metrics["sources"]["all"]["both_accuracy"])}.',
                  f'Podíl odpovědí neurčeno: {pct(metrics["sources"]["all"]["unknown_rate"])}.',
                  '', '## Srovnání s heuristikou', '',
                  f'Referenční sada: shoda podrobných kategorií {pct(metrics["heuristic_agreement"]["fine"]["accuracy"])}, hlavních kategorií {pct(metrics["heuristic_agreement"]["main"]["accuracy"])}.',
                  'Tato shoda není přesnost: heuristika obsahuje neurčené a širší kategorie.',
                  (f'Celkové hodnocení zahrnuje {metrics["prompt_development_overlap"]} transakcí z dřívějšího pilotu. Řádek excluding_pilot je vylučuje.'
                   if pilot_ids else 'V tomto experimentu nejsou označené transakce použité při vývoji promptu.'),
                  '', '## Nejčastější záměny podrobných kategorií', ''])
    top=[r for r in confusions if r['source']=='all' and r['level']=='fine' and r['target']!=r['prediction']][:12]
    for r in top:lines.append(f'- {dictionary[r["target"]]["Kategorie"]} → {dictionary[r["prediction"]]["Kategorie"]}: {r["count"]}')
    lines.extend(['','## Metodika a omezení','',
                  f'- Model dostal pevnou taxonomii {len(dictionary)} kategorií a {len(groups)} hlavních skupin, nikoli referenční štítky transakcí ani katalog obchodníků.',
                  '- Posuzoval jednu dávku nezávislých transakcí v jednom požadavku. Dávky neznamenají společného člověka.',
                  '- Použité bankovní údaje: datum provedení, protistrana, zaúčtovaná částka a měna, typ operace a obě poznámky. Ostatní sloupce (např. původní měna před přepočtem) do tohoto experimentu nevstupují.',
                  '- Scénáře referenční sady byly obnoveny až po přesné reprodukci všech bankovních údajů; bankovní výpisy se nepřepisovaly.',
                  '- Vstupy neobsahují položky účtenky. Například smíšený obchod, hotel či prodejce vstupenek nemusí jednoznačně určit podrobnou scénářovou kategorii.',
                  '- Výsledek hodnotí tento syntetický dataset. Z něj nelze vyvozovat stejnou přesnost u jiných lidí, bank nebo reálných plateb.',
                  '- Prompt a nastavení jsou uložené v run.json; identifikátory případných vývojových příkladů jsou v evaluation_context.prompt_development_ids.'])
    (output/'evaluation_report.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    if args.plots:
        import numpy as np
        import matplotlib.pyplot as plt
        codes=list(groups)
        indices={code:i for i,code in enumerate(codes)}
        matrix=np.zeros((len(codes),len(codes)),dtype=int)
        for row in enriched:
            matrix[indices[row['Kod hlavni kategorie scenare']],indices[row['Kod hlavni kategorie LLM']]]+=1
        denominators=matrix.sum(axis=1,keepdims=True)
        normalized=np.divide(100*matrix,denominators,out=np.zeros_like(matrix,dtype=float),where=denominators!=0)
        fig,ax=plt.subplots(figsize=(11,9))
        im=ax.imshow(normalized,cmap='Blues',vmin=0,vmax=100)
        ax.set_xticks(range(len(codes)),codes,rotation=45,ha='right')
        ax.set_yticks(range(len(codes)),[f'{code}: {groups[code]}' for code in codes])
        for i in range(len(codes)):
            for j in range(len(codes)):
                if normalized[i,j]>=1:
                    ax.text(j,i,f'{normalized[i,j]:.0f}',ha='center',va='center',color='white' if normalized[i,j]>55 else 'black',fontsize=8)
        ax.set(title='Hlavní kategorie: procenta v rámci scénářové skupiny',xlabel=f'Predikce {model}',ylabel='Scénář generátoru')
        fig.colorbar(im,ax=ax,label='% scénářové skupiny')
        fig.tight_layout();fig.savefig(output/'main_confusion.png',dpi=160);plt.close(fig)
        selected=sorted(metrics['sources']['all']['fine']['per_class'],key=lambda r:r['support'],reverse=True)[:20]
        fig,ax=plt.subplots(figsize=(12,8))
        y=np.arange(len(selected))
        ax.barh(y-.18,[100*r['precision'] for r in selected],height=.36,label='Precision')
        ax.barh(y+.18,[100*r['recall'] for r in selected],height=.36,label='Recall')
        ax.set_yticks(y,[dictionary[r['code']]['Kategorie']+f' (n={r["support"]})' for r in selected])
        ax.invert_yaxis();ax.set(xlim=(0,100),xlabel='%',title='20 nejčetnějších scénářových kategorií')
        ax.legend();fig.tight_layout();fig.savefig(output/'category_quality.png',dpi=160);plt.close(fig)
    if args.plots:
        with (output/'evaluation_report.md').open('a',encoding='utf-8') as handle:
            handle.write('\n## Grafy\n\n![Záměny hlavních kategorií](main_confusion.png)\n\n![Precision a recall nejčetnějších kategorií](category_quality.png)\n')
    print('\n'.join(lines[:13]),flush=True)


if __name__=='__main__':
    main()
