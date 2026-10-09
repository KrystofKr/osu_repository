"""Evaluate a model-proposed taxonomy without requiring identical label names."""
import argparse
import hashlib
import json
import math
from collections import Counter, defaultdict
from pathlib import Path

from data_paths import DATA, data_path
from evaluate_llm import scores, write_csv
from llm_utils import ID, INPUT_FIELDS, load_journal, load_taxonomy, read_csv, write_json


def partition_scores(pairs):
    """ARI and entropy metrics are invariant to renaming arbitrary cluster codes."""
    n = len(pairs)
    if not n:
        return {key: None for key in ('ari','homogeneity','completeness','v_measure','purity')}
    targets = Counter(a for a,b in pairs)
    clusters = Counter(b for a,b in pairs)
    cells = Counter(pairs)
    choose_two = lambda k: k*(k-1)/2
    total_pairs = choose_two(n)
    a = sum(choose_two(k) for k in targets.values())
    b = sum(choose_two(k) for k in clusters.values())
    expected = a*b/total_pairs if total_pairs else 0
    denominator = (a+b)/2-expected
    ari = (sum(choose_two(k) for k in cells.values())-expected)/denominator if denominator else 1.0
    entropy = lambda counts: -sum(k/n*math.log(k/n) for k in counts.values())
    target_entropy = entropy(targets)
    cluster_entropy = entropy(clusters)
    information = sum(k/n*math.log(k*n/(targets[t]*clusters[c])) for (t,c),k in cells.items())
    h = min(1.0,max(0.0,information/target_entropy)) if target_entropy else 1.0
    c = min(1.0,max(0.0,information/cluster_entropy)) if cluster_entropy else 1.0
    maxima = defaultdict(int)
    for (target,cluster),k in cells.items():
        maxima[cluster] = max(maxima[cluster],k)
    return {'ari':ari,'homogeneity':h,'completeness':c,'v_measure':2*h*c/(h+c) if h+c else 0.0,
            'purity':sum(maxima.values())/n,'target_classes':len(targets),'predicted_classes':len(clusters)}


def calibration_mapping(pairs, excluded=()):
    """Many-to-one majority association fitted only on the discovery/calibration split."""
    counts = defaultdict(Counter)
    for target, cluster in pairs:
        if cluster not in excluded:
            counts[cluster][target] += 1
    return {cluster:sorted(frequency, key=lambda t:(-frequency[t],t))[0]
            for cluster,frequency in counts.items()}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--experiment', type=Path, default=DATA/'experiments/qwen3.5_4b_discovered')
    parser.add_argument('--baseline', type=Path, default=DATA/'experiments/qwen3.5_4b_all_categories')
    parser.add_argument('--plots', action='store_true')
    args = parser.parse_args(argv)
    output = args.experiment.resolve()
    if (DATA/'experiments').resolve() not in output.parents:
        parser.error('Experiment musí být pod data/experiments/.')
    run = json.loads((output/'run.json').read_text())
    configuration = run['configuration']
    if configuration.get('taxonomy_mode') != 'model_proposed':
        raise ValueError('Tento evaluator vyžaduje model-proposed taxonomii.')
    for name,digest in configuration['input_hashes'].items():
        if hashlib.sha256(data_path(name).read_bytes()).hexdigest() != digest:
            raise ValueError('Vstupy se změnily: '+name)
    taxonomy_path = (DATA/configuration['taxonomy_path']).resolve()
    if (DATA/'experiments').resolve() not in taxonomy_path.parents or hashlib.sha256(taxonomy_path.read_bytes()).hexdigest() != configuration['taxonomy_sha256']:
        raise ValueError('Taxonomie se změnila nebo je mimo experimenty.')
    document, dictionary_rows, groups = load_taxonomy(taxonomy_path)
    dictionary = {r['Kod kategorie']:r for r in dictionary_rows}
    transactions = read_csv(data_path('data_combined.csv'))
    identities = {r[ID] for r in transactions}
    predictions = load_journal(output/'predictions.jsonl')
    if len(identities) != len(transactions) or set(predictions) != identities or run['completed'] != len(transactions):
        raise ValueError('Vyhodnocení vyžaduje dokončený, jednoznačný běh všech transakcí.')
    discovery_ids = set(document['sample_ids'])
    if not discovery_ids < identities or set(run['evaluation_context']['taxonomy_discovery_ids']) != discovery_ids:
        raise ValueError('Neplatné rozdělení na návrhový a hodnoticí vzorek.')
    scenarios = read_csv(data_path('reference_scenarios.csv')) + read_csv(data_path('synthetic_profiles.csv'))
    labels = {r[ID]:r for r in scenarios}
    mapping = {r['Puvodni kategorie']:r for r in read_csv(data_path('category_mapping.csv'))}
    if len(labels) != len(scenarios) or set(labels) != identities:
        raise ValueError('Scénáře nepokrývají jednoznačně výpis.')
    old_dictionary = {r['Kod kategorie']:r for r in read_csv(data_path('category_dictionary.csv'))}
    old_groups = {r['Kod hlavni kategorie']:r['Hlavni kategorie'] for r in read_csv(data_path('main_category_dictionary.csv'))}
    rows = []
    for transaction in transactions:
        identity = transaction[ID]
        prediction = predictions[identity]
        fine = prediction['Kod kategorie LLM']
        main = prediction['Kod hlavni kategorie LLM']
        if fine not in dictionary or main not in groups:
            raise ValueError('Neplatné kódy predikce.')
        gold = mapping[labels[identity]['Kategorie']]
        rows.append({ID:identity,'Sada':'discovery' if identity in discovery_ids else 'held_out',
                     'Zdroj':'reference' if identity.startswith('REF-') else 'synthetic',
                     **{f:transaction[f] for f in INPUT_FIELDS},
                     'Kod kategorie LLM':fine,'Kategorie LLM':dictionary[fine]['Kategorie'],
                     'Kod hlavni kategorie LLM':main,'Hlavni kategorie LLM':groups[main],
                     'Kod scenare':gold['Kod kategorie'],'Kategorie scenare':gold['Kategorie'],
                     'Kod hlavni kategorie scenare':gold['Kod hlavni kategorie'],
                     'Hlavni kategorie scenare':gold['Hlavni kategorie'],
                     'Konzistentni hierarchie':int(main==dictionary[fine]['Kod hlavni kategorie']),
                     'Neurceno':int(dictionary[fine]['Neurceno'])})
    subsets = {'all':rows,'discovery':[r for r in rows if r['Sada']=='discovery'],
               'held_out':[r for r in rows if r['Sada']=='held_out'],
               'reference':[r for r in rows if r['Zdroj']=='reference'],
               'synthetic':[r for r in rows if r['Zdroj']=='synthetic']}
    levels = [('fine','Kod scenare','Kod kategorie LLM'),
              ('main','Kod hlavni kategorie scenare','Kod hlavni kategorie LLM')]
    unknown = {r['Kod kategorie'] for r in dictionary_rows if r['Neurceno']}
    unknown_groups = {g for g in groups if all(r['Neurceno'] for r in dictionary_rows if r['Kod hlavni kategorie']==g)}
    aligned = {level:calibration_mapping([(r[target],r[pred]) for r in subsets['discovery']],
                                         unknown if level=='fine' else unknown_groups)
               for level,target,pred in levels}
    for row in rows:
        row['Kod scenare asociovany z navrhoveho vzorku'] = aligned['fine'].get(row['Kod kategorie LLM'],'')
        row['Kod hlavniho scenare asociovany z navrhoveho vzorku'] = aligned['main'].get(row['Kod hlavni kategorie LLM'],'')
    metrics = {'count':len(rows),'target':'Generator scenarios, not independently annotated real transactions',
               'taxonomy_fine_count':len(dictionary),'taxonomy_main_count':len(groups),
               'discovery_count':len(discovery_ids),'held_out_count':len(subsets['held_out']),
               'hierarchy_consistency':sum(r['Konzistentni hierarchie'] for r in rows)/len(rows),
               'unknown_rate':sum(r['Neurceno'] for r in rows)/len(rows),
               'calibration_mapping':aligned,'sources':{},'baseline':{},
               'mapping_policy':'Many-to-one majority fitted on discovery rows only; unknown/unseen clusters stay unmapped.'}
    for name,subset in subsets.items():
        metrics['sources'][name] = {'count':len(subset)}
        for level,target,pred in levels:
            pairs = [(r[target],r[pred]) for r in subset]
            values = partition_scores(pairs)
            values['mapped_scores'] = scores([(r[target],aligned[level].get(r[pred],'UNMAPPED')) for r in subset])
            values['mapping_coverage'] = sum(r[pred] in aligned[level] for r in subset)/len(subset) if subset else None
            metrics['sources'][name][level] = values
    baseline = load_journal(args.baseline.resolve()/'predictions.jsonl')
    baseline_run = json.loads((args.baseline.resolve()/'run.json').read_text())
    if set(baseline) != identities or baseline_run['configuration']['input_hashes'] != configuration['input_hashes']:
        raise ValueError('Baseline nemá stejné transakce a vstupní snapshot.')
    for level,target,pred in levels:
        pairs = [(r[target],baseline[r[ID]][pred]) for r in subsets['held_out']]
        metrics['baseline'][level] = {'partition':partition_scores(pairs),'fixed_label_scores':scores(pairs)}
    metrics['baseline']['batch_size'] = baseline_run['configuration']['batch_size']
    metrics['baseline']['model'] = baseline_run['configuration']['model']
    metrics['baseline']['digest'] = baseline_run['configuration']['digest']
    metrics['baseline']['run_sha256'] = hashlib.sha256((args.baseline/'run.json').read_bytes()).hexdigest()
    metrics['baseline']['predictions_sha256'] = hashlib.sha256((args.baseline/'predictions.jsonl').read_bytes()).hexdigest()
    frequencies = Counter(r['Kod kategorie LLM'] for r in rows)
    group_frequencies = Counter(r['Kod hlavni kategorie LLM'] for r in rows)
    unknown_category = next(r for r in document['categories'] if r['unknown'])
    unknown_parent = unknown_category['group']
    shared_unknown_parent = any(r['group']==unknown_parent and not r['unknown'] for r in document['categories'])
    metrics['unknown_taxonomy_parent'] = {'code':unknown_parent,'name':groups[unknown_parent],
                                        'shared_with_known_categories':shared_unknown_parent}
    taxonomy_rows=[]
    for category in document['categories']:
        code = category['code']
        counts = Counter(r['Kod scenare'] for r in rows if r['Kod kategorie LLM']==code)
        top = sorted(counts,key=lambda t:(-counts[t],t))[0] if counts else ''
        associated = aligned['fine'].get(code,'')
        taxonomy_rows.append({'Kod':code,'Kategorie':category['name'],'Definice':category['description'],
                              'Kod hlavni':category['group'],'Hlavni kategorie':groups[category['group']],
                              'Cetnost':frequencies[code],
                              'Cetnost held-out':sum(r['Kod kategorie LLM']==code for r in subsets['held_out']),
                              'Neurceno':int(category['unknown']),
                              'Asociovany scenar (jen navrhovy vzorek)':associated,
                              'Asociovana kategorie scenare':old_dictionary[associated]['Kategorie'] if associated else '',
                              'Nejcastejsi scenar (cela data, popisne)':old_dictionary[top]['Kategorie'] if top else '',
                              'Podil nejcastejsiho scenare':counts[top]/frequencies[code] if top else ''})
    main_rows = [{'Kod':r['code'],'Hlavni kategorie':r['name'],'Definice':r['description'],
                  'Cetnost':group_frequencies[r['code']]} for r in document['groups']]
    contingencies = [{'level':level,'scenario':t,'llm_category':c,'count':count}
                     for level,target,pred in levels
                     for (t,c),count in Counter((r[target],r[pred]) for r in rows).most_common()]
    write_json(output/'evaluation.json',metrics)
    write_csv(output/'predictions.csv',rows,list(rows[0]))
    write_csv(output/'category_dictionary.csv',taxonomy_rows,list(taxonomy_rows[0]))
    write_csv(output/'main_category_dictionary.csv',main_rows,list(main_rows[0]))
    write_csv(output/'contingency.csv',contingencies,['level','scenario','llm_category','count'])
    discovery = json.loads((taxonomy_path.parent/'discovery.json').read_text())
    sample_configuration = discovery['configuration']
    chunks = math.ceil(len(discovery_ids)/sample_configuration['chunk_size'])
    percent = lambda value:f'{100*value:.2f} %' if value is not None else '—'
    fmt = lambda value:f'{value:.4f}' if value is not None else '—'
    lines = ['# Kategorie navržené Qwenem','',
             f'Qwen navrhl {len(dictionary)} podrobných kategorií a {len(groups)} hlavních skupin z {len(discovery_ids)} neoznačených transakcí. '
             f'Zmrazenou taxonomií označil všech {len(rows)} transakcí. Samostatné hodnocení používá {len(subsets["held_out"])} řádků mimo návrhový vzorek.',
             '', 'Současný číselník, scénářové štítky, heuristika ani katalog obchodníků nevstoupily do návrhu ani klasifikace. '
             'Cílem hodnocení jsou scénáře syntetického generátoru, nikoli nezávisle ověřené reálné platby.',
             '', '## Parametry', '', '| Parametr | Hodnota |','|---|---|',
             f'| Model | {configuration["model"]} |', f'| Digest | `{configuration["digest"]}` |',
             f'| Ollama | {run["ollama_version"]} |',
             f'| Návrhový vzorek | Náhodný bez opakování, seed {sample_configuration["sample_seed"]}; {chunks} dílčích návrhů nejvýše po {sample_configuration["chunk_size"]} + sjednocení |',
             f'| Požadavky návrhu / odpovědi odmítnuté validací | {len(discovery["calls"])} / {sum(bool(c.get("validation_error")) for c in discovery["calls"])} |',
             f'| Temperature / seed inference | {configuration["options"]["temperature"]} / {configuration["options"]["seed"]} |',
             '| Thinking | Vypnuto v obou fázích |',
             f'| Kontext návrh / sjednocení / klasifikace | {discovery["configuration"]["proposal_options"]["num_ctx"]} / {discovery["configuration"]["merge_options"]["num_ctx"]} / {configuration["options"]["num_ctx"]} |',
             f'| Limit odpovědi návrh / sjednocení / plná klasifikační dávka | {discovery["configuration"]["proposal_options"]["num_predict"]} / {discovery["configuration"]["merge_options"]["num_predict"]} / {configuration["options"]["num_predict"]} |',
             f'| Dávka / workers | {configuration["batch_size"]} / {run["last_execution"]["workers"]} |',
             f'| Čas návrhu | {discovery["wall_seconds"]/60:.2f} min |',
             f'| Čas klasifikace | {run["wall_seconds"]/60:.2f} min |',
             f'| Požadavky klasifikace / dělení neplatných odpovědí | {run["requests"]} / {run["fallback_splits"]} |',
             '', 'Časy sčítají aktivní spuštění; nezahrnují pauzy ani vyhodnocení. Bankovní vstupy jsou stejných sedm sloupců jako v předchozích experimentech.',
             '', '## Hlavní skupiny', '', '| Kód | Název | Transakce |','|---|---|---:|']
    lines.extend(f'| {r["code"]} | {r["name"]} | {group_frequencies[r["code"]]} |' for r in document['groups'])
    lines.extend(['','## Podrobné kategorie','','| Kód | Kategorie | Skupina | Transakce |','|---|---|---|---:|'])
    lines.extend(f'| {r["code"]} | {r["name"]} | {groups[r["group"]]} | {frequencies[r["code"]]} |' for r in document['categories'])
    lines.extend(['','## Rozdělení transakcí mimo návrhový vzorek','',
                  '| Úroveň a experiment | ARI | Homogenita | Úplnost | V-measure | Purity |',
                  '|---|---:|---:|---:|---:|---:|'])
    for level,_,_ in levels:
        for name,values in [('Vlastní kategorie',metrics['sources']['held_out'][level]),
                            (f'Pevný číselník, dávka {metrics["baseline"]["batch_size"]}',metrics['baseline'][level]['partition'])]:
            lines.append(f'| {level}: {name} | {fmt(values["ari"])} | {percent(values["homogeneity"])} | {percent(values["completeness"])} | {percent(values["v_measure"])} | {percent(values["purity"])} |')
    lines.extend(['','ARI porovnává, zda stejné dvojice transakcí patří do stejných kategorií, s korekcí na náhodnou shodu. '
                  'Hodnota 1 znamená stejné rozdělení, kolem 0 náhodnou shodu. Nezávisí na názvech kategorií.',
                  'Homogenita popisuje čistotu kategorií vzhledem ke scénářům; úplnost ukazuje, zda se jeden scénář nerozpadá do více kategorií. '
                  'V-measure je jejich harmonický průměr. Purity je podíl většinového scénáře v každé kategorii; '
                  'je pouze popisná a lze ji zvýšit velkým počtem kategorií.',
                  '', 'Definice metrik: [dokumentace scikit-learn](https://scikit-learn.org/stable/modules/clustering.html#clustering-performance-evaluation). '
                  'Výpočet v tomto projektu používá standardní knihovnu Pythonu.',
                  '', '## Asociace s původními scénáři','',
                  f'Pro každou novou kategorii se pouze na {len(discovery_ids)} návrhových řádcích určil většinový scénář. '
                  'Tato statistická asociace je aplikována na ostatní řádky. Více kategorií se může asociovat se stejným scénářem. '
                  'Neurčené kategorie a kategorie nepozorované v kalibračním vzorku zůstávají bez asociace a při tomto měření se počítají jako neshoda. '
                  'Nejde o ručně ověřenou významovou ekvivalenci ani přímou přesnost původních kódů.',
                  '', '| Úroveň | Shoda asociovaného scénáře (held-out) | Macro-F1 | Pokrytí asociací |',
                  '|---|---:|---:|---:|'])
    for level,_,_ in levels:
        value=metrics['sources']['held_out'][level]
        lines.append(f'| {level} | {percent(value["mapped_scores"]["accuracy"])} | {percent(value["mapped_scores"]["macro_f1"])} | {percent(value["mapping_coverage"])} |')
    lines.extend(['',f'Konzistence hierarchie všech predikcí: {percent(metrics["hierarchy_consistency"])}. '
                  f'Neurčený účel: {percent(metrics["unknown_rate"])}. '
                  f'Použito {len(frequencies)} z {len(dictionary)} podrobných kategorií.',
                  '', '## Kontrola návrhu','',
                  f'Kategorie pro neurčitelný účel „{unknown_category["name"]}“ patří podle modelu do skupiny „{groups[unknown_parent]}“. '
                  + ('Tato skupina obsahuje i kategorie známých účelů, takže neznámé platby nelze na hlavní úrovni oddělit od známých účelů této skupiny. '
                     if shared_unknown_parent else 'Neurčený účel má samostatnou hlavní skupinu. ')
                  + 'Návrh byl zachován bez ručního přesunu. Konzistence hierarchie kontroluje jen dodržení vazby, nikoli správnost jejího významu.',
                  '', '## Soubory a omezení','',
                  '- `taxonomy.json` obsahuje původní názvy a definice Qwenu; kódy D/H přidělil skript. Číselníky projektu se nemění.',
                  '- `discovery.json` a `proposal_*.json` uchovávají vzorek, prompty, nastavení a odpovědi návrhové fáze.',
                  '- `category_dictionary.csv` a `main_category_dictionary.csv` obsahují vlastní číselníky s četnostmi.',
                  '- `predictions.csv` obsahuje všechny bankovní řádky, nové štítky a odděleně scénářové štítky pro kontrolu.',
                  '- `evaluation.json` obsahuje také metriky všech řádků, návrhového vzorku a obou zdrojových sad.',
                  '- `contingency.csv` ukazuje celé křížení nových kategorií a scénářů.',
                  '- Návrh z náhodného vzorku může vynechat vzácné účely. Zmrazená taxonomie se při klasifikaci nedoplňuje.',
                  '- Scénářový záměr někdy nelze určit z bankovního textu. Přiměřené širší kategorie mohou mít horší shodu s podrobnými scénáři.',
                  '- S předchozím během se mění taxonomie i instrukce, jde tedy o porovnání celých postupů, nikoli izolovaný vliv počtu kategorií.',
                  '- Transakce mimo návrhový vzorek sdílejí syntetické obchodníky a generátor s návrhovými. Nejde o test generalizace na nové obchodníky či reálná data.'])
    if args.plots:
        import numpy as np
        import matplotlib.pyplot as plt
        ordered=sorted(taxonomy_rows,key=lambda r:r['Cetnost'],reverse=True)
        fig,ax=plt.subplots(figsize=(12,max(7,len(ordered)*.25)))
        ax.barh([r['Kategorie'] for r in ordered],[r['Cetnost'] for r in ordered])
        ax.invert_yaxis();ax.set(xlabel='Počet transakcí',title='Kategorie navržené Qwenem')
        fig.tight_layout();fig.savefig(output/'category_frequencies.png',dpi=160);plt.close(fig)
        targets=list(old_groups);custom=list(groups)
        matrix=np.zeros((len(targets),len(custom)))
        for row in rows:
            matrix[targets.index(row['Kod hlavni kategorie scenare']),custom.index(row['Kod hlavni kategorie LLM'])]+=1
        denominator=matrix.sum(axis=1,keepdims=True)
        normalized=np.divide(100*matrix,denominator,out=np.zeros_like(matrix),where=denominator!=0)
        fig,ax=plt.subplots(figsize=(max(10,len(custom)*.7),10))
        im=ax.imshow(normalized,cmap='Blues',vmin=0,vmax=100,aspect='auto')
        ax.set_xticks(range(len(custom)),[groups[c] for c in custom],rotation=55,ha='right')
        ax.set_yticks(range(len(targets)),[old_groups[c] for c in targets])
        ax.set(xlabel='Vlastní skupina Qwenu',ylabel='Scénářová skupina',title='Podíl scénářové skupiny v nových skupinách (%)')
        fig.colorbar(im,ax=ax);fig.tight_layout();fig.savefig(output/'main_contingency.png',dpi=160);plt.close(fig)
        lines.extend(['','## Grafy','','![Četnosti kategorií](category_frequencies.png)','',
                      '![Křížení hlavních skupin](main_contingency.png)'])
    (output/'evaluation_report.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    summary = {'categories':len(dictionary),'main_groups':len(groups),'labeled':len(rows),
               'held_out':len(subsets['held_out']), 'levels':{}}
    for level,_,_ in levels:
        value=metrics['sources']['held_out'][level]
        summary['levels'][level]={key:value[key] for key in ['ari','homogeneity','completeness','v_measure']}
        summary['levels'][level]['mapped_scenario_agreement']=value['mapped_scores']['accuracy']
    print(json.dumps(summary,ensure_ascii=False,indent=2))


if __name__=='__main__':
    main()
