"""Label the synthetic reference transactions using explicit, reviewable rules; no demographic inference."""
from data_paths import data_path, PROFILE_COLUMNS
import csv,re,unicodedata
from decimal import Decimal
from collections import Counter, defaultdict
def norm(text):
    return ''.join(c for c in unicodedata.normalize('NFKD',text.lower()) if not unicodedata.combining(c))
def has(text,*terms):return any(norm(t) in text for t in terms)
from generate_synthetic import PROFILES
persons = {norm(profile[1]) for profile in PROFILES}
def classify(r):
    merchant=norm(r['Nazev protiuctu']);kind=norm(r['Typ transakce']);note=norm(r['Zprava pro prijemce']+' '+r['Popis pro me']);alltext=merchant+' '+note
    def result(cat,evidence,certainty='vysoká'):return cat,certainty,evidence
    # Operation semantics outrank the merchant (e.g. returns versus shopping).
    if has(kind,'vrácení'): return result('vratka nákupu','Typ transakce: vrácení nákupu')
    if has(kind,'výběr'):return result('výběr hotovosti','Typ transakce: výběr z bankomatu')
    if 'vklad' in kind:return result('vklad hotovosti','Typ transakce: vklad přes ATM')
    if has(kind,'srážková'):return result('daň z úroku','Typ transakce: srážková daň')
    if has(kind,'připsaný'):return result('přijatý úrok','Typ transakce: připsaný úrok')
    if has(kind,'odepsaný'):return result('úroky z úvěru','Typ transakce: odepsaný úrok')
    if 'poplatek' in kind:return result('bankovní poplatky','Typ transakce: poplatek')
    if has(kind,'vyrovnávací'):return result('vyrovnávací úhrada','Typ transakce: vyrovnávací úhrada')
    if has(note,'mzdy') or has(merchant,'zúčtování se zaměstnanci','zúčt.se zam.'):
        return result('mzda','Poznámka Mzdy nebo mzdový název protistrany')
    if has(note,'dividend'):return result('dividendy','Zpráva obsahuje dividend')
    if has(note,'cash sale') or has(alltext,'nákup akci','úpis akci'):return result('investice','Text výslovně odkazuje na akcie/prodej cenných papírů')
    if has(alltext,'splátka'):return result('splátka úvěru','Výslovná poznámka o splátce; včetně ALZA PC')
    if 'alza pc' in note:return result('splátka úvěru','Pravidelná platba ALZA PC','střední')
    if has(note,'školné'):return result('vzdělávání','Poznámka o školném')
    if has(note,'servis kotle','revize tc'):return result('opravy domácnosti','Výslovná poznámka servis kotle/revize TC')
    if has(alltext,'pojist','pojišť','vzp'):return result('pojištění','Protistrana nebo zpráva o pojištění')
    if has(alltext,'čez','platba ele zakaznicke'):return result('energie','Protistrana ČEZ nebo platba elektřiny')
    if has(note,'odběrné místo'):return result('energie','Záloha s odběrným místem','střední')
    if re.search(r'\b(?:dar|darek|darky)\b', note) and 'ecmc' not in note:return result('dárky','Výslovná poznámka dar/dárek')
    if has(note,'proplaceni dokladu') or has(merchant,'závazky-pracovní cesty'):return result('náhrada výdajů','Výslovná poznámka náhrady/proplacení dokladů')
    if has(alltext,'rohlik','wwwrohlik','velka pecka','kosik.','billa','albert','tesco','lidl','penny','potravin','minimarket','market 01','db market','mily market','hruska 498','smisene zbozi','p-l vinamex','reznictvi','delmart','sonnentor','manutea','thechillidoctor','erebosdrink'):
        return result('potraviny','Identifikovatelný potravinářský obchod nebo objednávka potravin')
    if has(merchant,'pidlitacka','operator ict','dpp -','csad'):return result('veřejná doprava','Dopravce nebo aplikace jízdného')
    if has(merchant,'cd ','www.cd.cz','ceske drahy','regiojet','rjcz'):return result('vlak','Železniční dopravce')
    if has(merchant,'tsk praha'):return result('parkování','TSK Praha','střední')
    if has(alltext,'jidlopodnos','speedlo'):return result('rozvoz jídla','Objednávka rozvozu jídla')
    if has(merchant,'steam','gamivo','epic games','xzone'):return result('hry','Herní obchod')
    if has(merchant,'openai','patreon'):return result('předplatné','Poskytovatel digitálního předplatného')
    if has(merchant,'codecademy','isibalo','fsv cvut'):return result('vzdělávání','Vzdělávací poskytovatel')
    if has(merchant,'lekarn','lekarna','dr. max'):return result('léky','Lékárna; konkrétní nákup není znám','střední')
    if has(merchant,'iscare gastro'):return result('zdravotní péče','Zdravotnické zařízení')
    if has(merchant,'super zoo'):return result('chovatelské potřeby','Prodejna potřeb pro zvířata; konkrétní položka není známa','střední')
    if has(merchant,'teta','rossmann'):return result('drogerie','Drogerie')
    if has(alltext,'bauhaus','hornbach','pro-doma','barvy-laky','barvy'):return result('dům a zahrada','Hobby prodejna nebo stavební materiály','střední')
    if has(merchant,'intersport','decasport','sportovni-poha') or has(note,'4camping'):return result('sportovní vybavení','Sportovní obchod','střední')
    if has(merchant,'gymbeam','brainmarket'):return result('výživa a doplňky','Prodejce výživy/doplňků; konkrétní položka není známa','střední')
    if has(merchant,'aquapalace','wellness'):return result('sport a wellness','Sportovní/wellness zařízení')
    if has(merchant,'papirnictvi','hracky a papir'):return result('papírnictví a hračky','Smíšený sortiment papírnictví/hračky','střední')
    if has(merchant,'kvetiny'):return result('květiny','Květinářství')
    if has(merchant,'alza','action','b058','obchodni dum','galerie harfa','ouShop','shoptet') or has(note,'alza.cz'):
        return result('smíšený maloobchod','Obchod s více kategoriemi; obsah nákupu není doložen','střední')
    if has(note,'datart','e-elektro'):return result('elektronika','Objednávka u prodejce elektroniky','střední')
    if has(merchant,'posta','zasilkovna','ppl ','dpd ','gls ','dhl ','geis '):return result('poštovné a zásilky','Dopravce zásilek; může jít o dobírku','střední')
    if has(merchant,'gopay','comgate','sumup'):return result('neurčeno','Platební brána neidentifikuje obsah nákupu','nízká')
    if has(merchant,'goout','storm club','(a)void','zo praha','joystick'):return result('kultura a volný čas','Kulturní zařízení/prodej vstupenek; konkrétní událost neznámá','střední')
    if has(merchant,'hotel','almanac'):return result('hotelové služby','Hotel může účtovat ubytování i restauraci','střední')
    if has(merchant,'cafe','kafe','kava','kavarna','cake art','parlor','la zmr','cajovna','bb ','delikomat','pekarna'):
        return result('kavárny a občerstvení','Název kavárny, pekárny nebo občerstvení','střední')
    if has(merchant,'restaur','bistro','burger','kebab','pizza','pizzer','gastro','canteen','kantyna','pho ','namastaey','indicka','takumi','plzenka','pivovar','husa catering','mcdonald','bageterie','tung ','moris','red bean','zen stod','lokal','nyx*practical','neu*practical','minipivovar','nemy medved','mianchi','leknin','zariva','bertka','veget'):
        return result('restaurace','Gastronomický název protistrany','střední')
    bare=re.sub(r'^(ing\.|rndr\.)\s*','',merchant)
    if bare in persons:return result('osobní převod','Smyšlená osobní protistrana; účel neurčen','střední')
    return result('neurčeno','Chybí jednoznačný účel nebo rozpoznaná protistrana','nízká')

def main():
    with data_path('data_all.csv').open(encoding='utf-8',newline='') as f: rows=list(csv.DictReader(f,delimiter=';'))
    # Fail early if a future import has damaged text; do not classify corrupted values.
    if any(chr(0xFFFD) in value for row in rows for value in row.values()):
        raise ValueError('data_all.csv obsahuje poškozené znaky. Opravte kódování zdrojových dat.')
    header = PROFILE_COLUMNS
    groups=defaultdict(list)
    for row in rows:groups[row['Identifikace transakce']].append(row)
    metadata=[];audit=[];seen=set()
    for r in rows:
        category,confidence,evidence=classify(r)
        ident=r['Identifikace transakce']
        if ident in seen:continue
        seen.add(ident)
        group=groups[ident]
        if len(group)>1 and not (len(group)==2 and {x['Mena'] for x in group}=={'CZK','EUR'} and all(has(norm(x['Typ transakce']), 'vyrovnávací') for x in group) and Decimal(group[0]['Castka'].replace(',','.'))*Decimal(group[1]['Castka'].replace(',','.'))<0):
            raise ValueError(f'Nejednoznačný duplicitní identifikátor transakce: {ident}')
        if len(group)==2 and {x['Mena'] for x in group}=={'CZK','EUR'} and all('vyrovn' in norm(x['Typ transakce']) for x in group) and Decimal(group[0]['Castka'].replace(',','.'))*Decimal(group[1]['Castka'].replace(',','.'))<0:
            category,confidence,evidence='směna měn','vysoká','Dvě měnové nohy vyrovnávací úhrady se společným identifikátorem'
        metadata.append(dict(zip(header,[r['Identifikace transakce'],'R00','','Syntetická reference – heuristický odhad',category,1,('FX-'+ident) if category=='směna měn' else ''])))
        audit.append({'Identifikace transakce':r['Identifikace transakce'],'Kategorie':category,'Jistota':confidence,'Duvod':evidence,'Nazev protiuctu':r['Nazev protiuctu']})
    def write(name,header,items):
        data_path(name).parent.mkdir(parents=True, exist_ok=True)
        with data_path(name).open('w',encoding='utf-8',newline='') as f:
            wr=csv.DictWriter(f,fieldnames=header,delimiter=';');wr.writeheader();wr.writerows(items)
    assert len(seen)==len(groups)
    assert len(metadata)==len(groups) and all(set(x)==set(header) for x in metadata)
    write('original_profiles.csv',header,metadata)
    write('original_classification_audit.csv',list(audit[0]),audit)
    for name in ['original_profiles.csv','original_classification_audit.csv']:
        with data_path(name).open(encoding='utf-8',newline='') as f:loaded=list(csv.DictReader(f,delimiter=';'))
        assert len(loaded)==len(groups) and {r['Identifikace transakce'] for r in loaded}=={r['Identifikace transakce'] for r in rows}
    lookup={r['Identifikace transakce']:r for r in metadata}
    assert len(lookup)==len(metadata)
    assert len([lookup[r['Identifikace transakce']] for r in rows])==len(rows)
    counts=Counter(lookup[r['Identifikace transakce']]['Kategorie'] for r in rows)
    print(f'Original rows: {len(rows)}; metadata IDs: {len(metadata)}; classified rows: {len(rows)-counts["neurčeno"]}; unknown: {counts["neurčeno"]}')


if __name__ == "__main__":
    main()
