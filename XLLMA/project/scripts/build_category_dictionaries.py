"""Build shared category codebooks and frequencies without changing transaction labels."""
from data_paths import require_synthetic_reference, data_path
import csv
from collections import Counter
def read(name):
    with data_path(name).open(encoding='utf-8',newline='') as f:return list(csv.DictReader(f,delimiter=';'))
def write(name,rows):
    data_path(name).parent.mkdir(parents=True, exist_ok=True)
    with data_path(name).open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter=';');w.writeheader();w.writerows(rows)
ALIASES={'poštovné':'poštovné a zásilky','kavárny':'kavárny a občerstvení'}
GROUPS={
    'G01':('Příjmy',['mzda','důchod','rodičovský příspěvek','stipendium a brigáda','příjmy z podnikání','náhrada výdajů']),
    'G02':('Bydlení a domácnost',['nájem nebo hypotéka','energie','nábytek','domácí potřeby','opravy domácnosti','servis spotřebičů','úklidové služby','prádelna','dům a zahrada','zahrada']),
    'G03':('Potraviny a stravování',['potraviny','restaurace','kavárny a občerstvení','rozvoz jídla']),
    'G04':('Nákupy a osobní péče',['drogerie','oblečení','obuv','elektronika','smíšený maloobchod','kadeřnictví','kosmetické služby','květiny','dárky']),
    'G05':('Doprava',['veřejná doprava','vlak','taxi','pohonné hmoty','autoservis','parkování','mytí auta']),
    'G06':('Zdraví',['léky','zdravotní péče','zubař','fyzioterapie','optika','psychoterapie','výživa a doplňky']),
    'G07':('Sport, kultura a volný čas',['sport','sport a wellness','sportovní vybavení','kultura a volný čas','kino','divadlo','koncerty','knihy','hry']),
    'G08':('Vzdělávání a děti',['vzdělávání','školní potřeby','papírnictví a hračky','hračky','péče o děti']),
    'G09':('Zvířata',['chovatelské potřeby','krmivo','veterinář','péče o zvířata']),
    'G10':('Cestování',['dovolená – letenky','dovolená – ubytování','dovolená – pronájem auta','dovolená – stravování','dovolená – suvenýry','dovolená – výlety','hotelové služby','cestovní pojištění']),
    'G11':('Komunikace a digitální služby',['telefon a internet','předplatné']),
    'G12':('Finance a pojištění',['pojištění','splátka úvěru','bankovní poplatky','úroky z úvěru','přijatý úrok','daň z úroku','investice','dividendy']),
    'G13':('Převody a hotovost',['osobní převod','směna měn','vyrovnávací úhrada','výběr hotovosti','vklad hotovosti','vratka nákupu']),
    'G14':('Ostatní služby a dary',['poštovné a zásilky','právní služby','účetnictví','charita']),
    'G99':('Neurčeno',['neurčeno']),
}
def main():
    all_group_categories = [cat for _, cats in GROUPS.values() for cat in cats]
    if len(all_group_categories) != len(set(all_group_categories)):
        raise ValueError('Kategorie je přiřazena více hlavním skupinám.')
    group_for={c:(code,name) for code,(name,cats) in GROUPS.items() for c in cats}
    reference_meta=read('original_profiles.csv');synthetic_meta=read('synthetic_profiles.csv');reference=read('data_all.csv');synthetic=read('data_synthetic.csv')
    require_synthetic_reference(reference)
    if any(r["Synteticka"] != "1" for r in reference_meta + synthetic_meta):
        raise ValueError("Obě datové sady musejí být označené jako syntetické.")
    def index(rows):
        out={r['Identifikace transakce']:r for r in rows}
        assert len(out)==len(rows), 'Metadata must have unique identifiers'
        return out
    if not reference or not synthetic:
        raise ValueError('Oba zdrojové výpisy musí obsahovat transakce.')
    om=index(reference_meta);sm=index(synthetic_meta)
    if set(om) & set(sm):
        raise ValueError('Identifikátory referenční a hlavní syntetické sady se překrývají.')
    assert set(om)=={r['Identifikace transakce'] for r in reference}
    assert set(sm)=={r['Identifikace transakce'] for r in synthetic}
    def canonical(category):return ALIASES.get(category,category)
    oc=Counter(canonical(om[r['Identifikace transakce']]['Kategorie']) for r in reference)
    sc=Counter(canonical(sm[r['Identifikace transakce']]['Kategorie']) for r in synthetic)
    oi=Counter(canonical(r['Kategorie']) for r in reference_meta)
    si=Counter(canonical(r['Kategorie']) for r in synthetic_meta)
    # Preserve previous category codes, including temporarily absent categories.
    existing=read('category_dictionary.csv') if data_path('category_dictionary.csv').exists() else []
    codes={r['Kategorie']:r['Kod kategorie'] for r in existing}
    assert len(codes)==len(existing), 'Duplicate category names in dictionary'
    if len(set(codes.values())) != len(codes):
        raise ValueError('Duplicitní kódy kategorií v číselníku.')
    categories=sorted(set(oc)|set(sc)|set(codes))
    assert set(categories)<=set(group_for),set(categories)-set(group_for)
    next_code=max([int(c[1:]) for c in codes.values()]+[0])+1
    for cat in categories:
        if cat not in codes:codes[cat]=f'K{next_code:03d}';next_code+=1
    result=[]
    for cat in categories:
        group_code,group_name=group_for[cat]
        result.append({'Kod kategorie':codes[cat],'Kategorie':cat,'Kod hlavni kategorie':group_code,'Hlavni kategorie':group_name,
        'Cetnost originalni radky':oc[cat],'Cetnost originalni identifikatory':oi[cat],
        'Cetnost synteticke radky':sc[cat],'Cetnost synteticke identifikatory':si[cat],
        'Cetnost spolecne radky':oc[cat]+sc[cat],
        'Podil originalni procent':f'{100*oc[cat]/len(reference):.2f}'.replace('.',','),
        'Podil synteticke procent':f'{100*sc[cat]/len(synthetic):.2f}'.replace('.',','),
        'Podil spolecne procent':f'{100*(oc[cat]+sc[cat])/(len(reference)+len(synthetic)):.2f}'.replace('.',',')})
    write('category_dictionary.csv',result)
    mapping=[]
    for label in sorted({r['Kategorie'] for r in reference_meta+synthetic_meta}):
        cat=canonical(label)
        mapping.append({'Puvodni kategorie':label,'Kod kategorie':codes[cat],'Kategorie':cat,'Kod hlavni kategorie':group_for[cat][0],'Hlavni kategorie':group_for[cat][1]})
    write('category_mapping.csv',mapping)
    main=[]
    for code,(name,_) in GROUPS.items():
        members=[r for r in result if r['Kod hlavni kategorie']==code]
        row={'Kod hlavni kategorie':code,'Hlavni kategorie':name,'Pocet kategorii':len(members)}
        for col in ['Cetnost originalni radky','Cetnost originalni identifikatory','Cetnost synteticke radky','Cetnost synteticke identifikatory','Cetnost spolecne radky']:
            row[col]=sum(r[col] for r in members)
        main.append(row)
    write('main_category_dictionary.csv',main)
    assert sum(r['Cetnost originalni radky'] for r in result)==len(reference)
    assert sum(r['Cetnost originalni identifikatory'] for r in result)==len(reference_meta)
    assert sum(r['Cetnost synteticke radky'] for r in result)==len(synthetic)
    assert len(set(codes.values()))==len(codes)
    for name in ['category_dictionary.csv','category_mapping.csv','main_category_dictionary.csv']:
        check=read(name);assert check and all(None not in r and None not in r.values() for r in check)
    print('Categories:',len(categories),'reference:',len(oc),'synthetic:',len(sc),'main groups:',len(main))
    print('Frequency totals:',len(reference),len(reference_meta),len(synthetic),len(reference)+len(synthetic))
    print('Top combined:',[(r['Kategorie'],r['Cetnost spolecne radky']) for r in sorted(result,key=lambda r:r['Cetnost spolecne radky'],reverse=True)[:5]])


if __name__ == "__main__":
    main()
