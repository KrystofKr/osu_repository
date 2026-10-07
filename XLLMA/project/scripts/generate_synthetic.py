"""Generate reproducible fictional bank transactions and their analysis metadata."""
from pathlib import Path
from data_paths import data_path, PROFILE_COLUMNS
from datetime import date, timedelta
from decimal import Decimal, ROUND_HALF_UP
import json
import math
import csv
import random

SEED = 20261009
START, END = date(2022, 1, 1), date(2026, 10, 5)
TARGET = 9000
PROFILES = [
    ('S01', 'Eliška Dubová', 'studentka', 14000, 6500, .65),
    ('S02', 'Matěj Skalický', 'mladý zaměstnanec', 34000, 12500, 1.0),
    ('S03', 'Veronika Lipová', 'rodina s dětmi', 57000, 18000, 1.4),
    ('S04', 'Antonín Jedlička', 'důchodce', 21500, 5500, .65),
    ('S05', 'Nela Kaštanová', 'podnikatelka', 78000, 16500, 1.65),
    ('S06', 'Šimon Bukovský', 'častý cestovatel', 62000, 14500, 1.5),
    ('S07', 'Zuzana Olšová', 'rodič na rodičovské', 23000, 8500, .8),
    ('S08', 'Dominik Borový', 'motorista', 46000, 11500, 1.15),
    ('S09', 'Amálie Modřínová', 'kultura a gastronomie', 41000, 13000, 1.2),
    ('S10', 'Vít Topolský', 'sportovec', 39000, 10500, 1.05),
    ('S11', 'Karolína Cedrová', 'domácnost se zvířaty', 36000, 11000, 1.0),
    ('S12', 'Richard Jasanový', 'vysokopříjmová domácnost', 105000, 27000, 2.0),
]
# Category, spending interval and base sampling weight.
BASKET = [
    ('potraviny', 80, 1900, 18),
    ('drogerie', 60, 950, 5),
    ('restaurace', 140, 1500, 8),
    ('kavárny', 45, 320, 7),
    ('rozvoz jídla', 180, 700, 5),
    ('oblečení', 200, 2800, 4),
    ('obuv', 500, 3200, 2),
    ('elektronika', 300, 24000, 1),
    ('nábytek', 600, 18000, 1),
    ('domácí potřeby', 80, 1900, 3),
    ('opravy domácnosti', 700, 14000, 1),
    ('úklidové služby', 500, 2500, 2),
    ('kadeřnictví', 250, 1900, 2),
    ('kosmetické služby', 400, 2400, 1),
    ('prádelna', 150, 900, 1),
    ('servis spotřebičů', 500, 6500, 1),
    ('léky', 70, 1500, 3),
    ('zubař', 600, 12000, 1),
    ('fyzioterapie', 600, 1600, 1),
    ('optika', 500, 8500, 1),
    ('psychoterapie', 900, 1800, 1),
    ('veřejná doprava', 20, 550, 7),
    ('vlak', 60, 1400, 4),
    ('taxi', 120, 950, 2),
    ('pohonné hmoty', 450, 2300, 4),
    ('autoservis', 800, 18000, 1),
    ('parkování', 20, 300, 3),
    ('mytí auta', 100, 450, 1),
    ('sport', 120, 1700, 3),
    ('sportovní vybavení', 200, 7500, 2),
    ('kino', 160, 650, 2),
    ('divadlo', 250, 1800, 2),
    ('koncerty', 250, 3000, 2),
    ('knihy', 120, 1400, 3),
    ('hry', 80, 1800, 2),
    ('vzdělávání', 400, 12000, 2),
    ('školní potřeby', 60, 1600, 2),
    ('péče o děti', 300, 4500, 2),
    ('hračky', 100, 2500, 2),
    ('veterinář', 400, 6500, 1),
    ('krmivo', 150, 2300, 2),
    ('péče o zvířata', 350, 1600, 1),
    ('zahrada', 90, 3700, 2),
    ('dárky', 150, 4500, 2),
    ('charita', 100, 1500, 1),
    ('právní služby', 1000, 9500, 1),
    ('účetnictví', 900, 5500, 1),
    ('poštovné', 60, 350, 2),
]

def main():
    RNG = random.Random(SEED)
    CATALOG = json.loads(Path(__file__).with_name("merchant_catalog.json").read_text())
    CATALOG = {
        category: [item for item in items if item.get("enabled_for_generation", False)]
        for category, items in CATALOG.items()
    }
    if any(not items for items in CATALOG.values()):
        raise ValueError("Každá kategorie musí mít ověřeného poskytovatele nebo výslovně smyšlenou osobu.")
    with data_path('data_all.csv').open(encoding='utf-8',newline='') as f:
        reader=csv.DictReader(f,delimiter=';'); HEADER=reader.fieldnames; ORIGINAL=list(reader)
    if not ORIGINAL:
        raise ValueError('Původní výpis je prázdný; nelze odvodit četnost poznámek.')
    ROWS, META = [], []
    ACCOUNTS={}
    def account(key):
        if key not in ACCOUNTS: ACCOUNTS[key]=f'{8800000000+len(ACCOUNTS)+1}/9999'
        return ACCOUNTS[key]
    def number(value):
        return format(Decimal(str(value)).quantize(Decimal('.01'),rounding=ROUND_HALF_UP),'f').replace('.',',')
    PROFILE_MERCHANTS = {}
    CARD_KINDS = {'Nákup u obchodníka', 'Nákup na internetu', 'Opakovaná platba', 'Vrácení nákupu', 'Výběr hotovosti z bankomatu'}
    ONLINE = {'rozvoz jídla','hry','vzdělávání','psychoterapie','dovolená – letenky','dovolená – ubytování','dovolená – výlety'}
    def add(profile,day,amount,merchant,category,kind='Platba kartou',currency='CZK',note=''):
        if day<START or day>END: return
        if category in CATALOG:
            choices=CATALOG[category]
            key=(profile[0],category)
            if kind=='Trvalý příkaz':
                if key not in PROFILE_MERCHANTS: PROFILE_MERCHANTS[key]=RNG.choice(choices)['name']
                merchant=PROFILE_MERCHANTS[key]
            else: merchant=RNG.choice(choices)['name']
        if kind=='Platba kartou': kind='Nákup na internetu' if category in ONLINE else 'Nákup u obchodníka'
        if category=='předplatné': kind='Opakovaná platba'
        if category=='vratka nákupu': kind='Vrácení nákupu'
        if category=='výběr hotovosti': kind='Výběr hotovosti z bankomatu'
        if category=='osobní převod': kind='Příchozí úhrada' if amount>0 else 'Odchozí úhrada'
        identity=f'SYN-{len(ROWS)+1:08d}'
        booked=min(day+timedelta(days=RNG.choice([0,1,1,2,3]) if kind in CARD_KINDS else 0),END)
        rate={'CZK':1,'EUR':24.8,'USD':22.7,'GBP':29.1,'PLN':5.8}[currency]
        # Masked cards identify the payer; bank transfers identify the beneficiary.
        card=f'4890 00** **** {9200+int(profile[0][1:])}'
        row=dict.fromkeys(HEADER,'')
        row.update({'Datum zauctovani':booked.strftime('%d.%m.%Y'),'Datum provedeni':day.strftime('%d.%m.%Y'),
        'Protistrana':card if kind in CARD_KINDS else account(merchant),'Nazev protiuctu':merchant,
        'Castka':number(Decimal(str(amount))*Decimal(str(rate))),'Mena':'CZK',
        'Identifikace transakce':identity,'Typ transakce':kind})
        if currency!='CZK': row.update({'Originalni castka':number(amount),'Originalni mena':currency,'Smenny kurz':number(rate)})
        if kind not in CARD_KINDS:
            row['VS']=str(710000000+int(profile[0][1:])*1000+list(CATALOG).index(category)) if kind=='Trvalý příkaz' else RNG.choice(['0',str(RNG.randrange(100000000,1000000000)),''])
        if kind in CARD_KINDS and kind!='Výběr hotovosti z bankomatu':
            # This is a modeled bank descriptor, not an asserted real acquiring descriptor.
            location='PARIS' if category in ['dovolená – suvenýry','dovolená – stravování','dovolená – pronájem auta'] else 'PRAHA'
            country='FRA' if location=='PARIS' else 'CZE'
            if currency=='EUR' and location!='PARIS': location,country='ONLINE','NLD'
            if merchant=='LEAL Papírnictví': location,country='LITOMERICE','CZE'
            if merchant=='GETYOURGUIDE': location,country='BERLIN','DEU'
            if merchant=='RYANAIR': location,country='DUBLIN','IRL'
            if merchant=='CODECADEMY': location,country='NEW YORK','USA'
            if merchant in ['STEAM PURCHASE','EPC*EPIC GAMES STORE']: location,country='ONLINE','USA'
            terminal='33' if kind=='Nákup na internetu' else '57' if kind=='Opakovaná platba' else '61' if kind=='Vrácení nákupu' else '51'
            msg=f'{merchant:<34} {location:<26} {country}  {terminal} {card}        ECMC    {day:%d.%m.%Y} {number(abs(amount)):>20} {currency}'
        elif kind=='Trvalý příkaz':
            msg={'energie':'ČEZ - ELEKTŘINA','pojištění':'ŽIVOTNÍ POJIŠTĚNÍ','nájem nebo hypotéka':'Nájem','telefon a internet':'Vyúčtování'}.get(category,'')
        elif kind=='Příchozí úhrada':
            msg=f'Mzdy {day.month}/{day.year}' if category=='mzda' else RNG.choice(['','dárek','vrácení peněz']) if category=='osobní převod' else ''
        elif kind=='Výběr hotovosti z bankomatu': msg=''
        else:
            msg=RNG.choice(['',f'Platba faktury {day.year}{RNG.randrange(10000,99999)}','QR Platba']) if category!='osobní převod' else RNG.choice(['','dárek','příspěvek'])
        if kind=='Výběr hotovosti z bankomatu': personal='Praha 1'
        elif category=='nájem nebo hypotéka': personal='nájem'
        elif category=='osobní převod': personal='dárek'
        elif category=='elektronika': personal=merchant
        else: personal=RNG.choice(['','platba','objednávka'])
        ROWS.append(row)
        META.append({'Identifikace transakce':identity,'Profil':profile[0],'Jmeno':profile[1],'Typ profilu':profile[2],'Kategorie':category,'Synteticka':1,'Skupina transakci':note,'_message':msg,'_personal':personal})
    for profile in PROFILES:
        pid,name,persona,income,rent,scale=profile
        for year in range(2022,2027):
            for month in range(1,13):
                first=date(year,month,1)
                if first>END: continue
                inflation=1+.045*(year-2022)
                salary='důchod' if persona=='důchodce' else 'rodičovský příspěvek' if 'rodičovské' in persona else 'stipendium a brigáda' if persona=='studentka' else 'příjmy z podnikání' if persona=='podnikatelka' else 'mzda'
                add(profile,date(year,month,4),income*inflation*RNG.uniform(.95,1.05),'',salary,'Příchozí úhrada')
                for day,amount,merchant,category in [(5,rent*inflation,'','nájem nebo hypotéka'),(8,1800*scale*inflation,'','energie'),(12,490*scale,'','telefon a internet'),(16,210*scale,'','předplatné'),(20,700*scale,'','pojištění')]:
                    add(profile,date(year,month,day),-amount,merchant,category,'Trvalý příkaz')
            # Related holiday purchases share a trip reference.
            for trip in range(2 if pid in ['S06','S12'] else 1):
                departure=date(year,RNG.choice([6,7,8]) if trip==0 else 2,RNG.randint(6,18))
                if departure>END: continue
                ref=f'Dovolená {pid}-{year}-{trip+1}'
                for delta,amount,merchant,category,currency in [(-55,4200,'','dovolená – letenky','CZK'),(-35,680,'','dovolená – ubytování','EUR'),(-7,480,'','cestovní pojištění','CZK'),(0,75,'','dovolená – pronájem auta','EUR'),(2,48,'','dovolená – stravování','EUR'),(3,35,'','dovolená – výlety','EUR'),(4,27,'','dovolená – suvenýry','EUR')]:
                    add(profile,departure+timedelta(days=delta),-amount*scale,merchant,category,currency=currency,note=ref)
    # Guarantee coverage of the entire consumer basket for the population.
    for i,(category,lo,hi,weight) in enumerate(BASKET):
        p=PROFILES[i%len(PROFILES)]
        add(p,START+timedelta(days=RNG.randrange((END-START).days+1)),-RNG.uniform(lo,hi),'',category)
    def weights(p,day):
        result=[]
        for category,lo,hi,base in BASKET:
            w=base
            if p[0] in ['S03','S07'] and category in ['péče o děti','hračky','školní potřeby','potraviny']: w*=4
            if p[0]=='S08' and category in ['pohonné hmoty','autoservis','parkování','mytí auta']: w*=7
            if p[0]=='S09' and category in ['divadlo','koncerty','restaurace','kino']: w*=5
            if p[0]=='S10' and category in ['sport','sportovní vybavení','fyzioterapie']: w*=6
            if p[0]=='S11' and category in ['veterinář','krmivo','péče o zvířata']: w*=8
            if p[0]=='S05' and category in ['účetnictví','právní služby','elektronika']: w*=6
            if p[0]=='S04' and category in ['léky','zahrada','optika']: w*=5
            if p[0]=='S01' and category in ['hry','veřejná doprava','knihy']: w*=4
            if day.month==12 and category in ['dárky','hračky','potraviny']: w*=3
            result.append(w)
        return result
    while len(ROWS)<TARGET:
        p=RNG.choices(PROFILES,weights=[.9,1,1.5,.7,1.2,1.5,.9,1.1,1.3,1.1,1,1.5])[0]
        day=START+timedelta(days=RNG.randrange((END-START).days+1))
        chance=RNG.random()
        if chance<.025:
            add(p,day,RNG.uniform(100,6500),'','vratka nákupu','Příchozí úhrada')
        elif chance<.05:
            add(p,day,-RNG.choice([500,1000,2000,3000,5000]),'','výběr hotovosti','Výběr z bankomatu')
        elif chance<.09:
            other=RNG.choice([x for x in PROFILES if x!=p])
            add(p,day,RNG.choice([-1,1])*RNG.uniform(100,4500),other[1],'osobní převod','Příchozí úhrada' if chance<.07 else 'Odchozí úhrada')

        else:
            category,lo,hi,_=RNG.choices(BASKET,weights=weights(p,day))[0]
            amount=lo+(hi-lo)*RNG.betavariate(1.2,3.5)
            amount*=p[5]*(1+.045*(day.year-2022))
            service=category in ['účetnictví','právní služby','opravy domácnosti','servis spotřebičů','péče o děti']
            add(p,day,-round(amount,2),'',category,'Odchozí úhrada' if service else 'Platba kartou')
    if len(ROWS) > TARGET:
        raise ValueError('Pravidelné platby a povinné kategorie překračují cílový počet transakcí.')
    # Fictional sparsity assumptions, independent of any private bank statement.
    def select_field(source_column, candidate, weight):
        count=round(TARGET*{'Zprava pro prijemce': .50, 'Popis pro me': .04}[source_column])
        eligible=[]
        for i,(row,meta) in enumerate(zip(ROWS,META)):
            if meta[candidate]: eligible.append((-math.log(max(RNG.random(),1e-12))/weight(row),i))
        assert len(eligible)>=count
        for _,i in sorted(eligible)[:count]: ROWS[i][source_column]=META[i][candidate]
    def message_weight(row):
        kind=row['Typ transakce'];year=int(row['Datum provedeni'][-4:])
        if kind in CARD_KINDS: return 1.0
        return .85 if kind=='Trvalý příkaz' else .35 if kind=='Odchozí úhrada' else .12
    select_field('Zprava pro prijemce','_message',message_weight)
    select_field('Popis pro me','_personal',lambda r: 15 if r['Typ transakce']=='Výběr hotovosti z bankomatu' else 1)
    for meta in META:
        del meta['_message'];del meta['_personal']
    def sortkey(row):
        return tuple(reversed(row['Datum zauctovani'].split('.')))+ (row['Identifikace transakce'],)
    def write(path,header,rows):
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open('w',encoding='utf-8',newline='') as f:
            writer=csv.DictWriter(f,fieldnames=header,delimiter=';');writer.writeheader();writer.writerows(rows)
    assert len(ROWS)==TARGET
    assert len({r['Identifikace transakce'] for r in ROWS})==TARGET
    assert not {r['Identifikace transakce'] for r in ROWS}&{r['Identifikace transakce'] for r in ORIGINAL}
    assert all(set(r)==set(HEADER) for r in ROWS)
    write(data_path('data_synthetic.csv'),HEADER,sorted(ROWS,key=sortkey))
    write(data_path('data_combined.csv'),HEADER,sorted(ORIGINAL+ROWS,key=sortkey))
    write(data_path('synthetic_profiles.csv'),PROFILE_COLUMNS,META)
    for filename,expected in [('data_synthetic.csv',TARGET),('data_combined.csv',len(ORIGINAL)+TARGET),('synthetic_profiles.csv',TARGET)]:
        with data_path(filename).open(encoding='utf-8',newline='') as f:
            reader=csv.DictReader(f,delimiter=';'); loaded=list(reader)
        assert len(loaded)==expected
        assert all(None not in row and None not in row.values() for row in loaded)
        print(f'{filename}: {expected} rows')
    print(f'Profiles: {len(PROFILES)}; categories: {len(set(r["Kategorie"] for r in META))}')


if __name__ == "__main__":
    main()
