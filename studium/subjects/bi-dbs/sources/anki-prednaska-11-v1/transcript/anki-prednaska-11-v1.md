# BI-DBS – Přednáška 11

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-dbs/BI-DBS.apkg; APKG SHA-256 2adef415f377fbe4eac7b4dd1e452577d8eedea5e207be2be6c2aeb0e90cf4eb. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 7f054157e2673745662b1c45d22f99de1a01232f0420fd85b7b7f7c2b095d969.
Původní balíčky: BI-DBS
Rozsah: 4 poznámek, 4 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1651509330500

Karty Anki: 1651509330500
GUID: wL/:_{it!9; štítky: bi-dbs::p11.

Metadata původního zdroje pro kartu 1651509330500: v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to ROWID?

### Odpověď (Back)

Je to unikátní identifikátor řádku. Využívá se pro implementaci indexů.

## Poznámka Anki 1651509553820

Karty Anki: 1651509553821
GUID: vrv7l9-/}$; štítky: bi-dbs::p11.

Metadata původního zdroje pro kartu 1651509553821: v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to index a jaké jsou jeho typy? Co je to selektivita klíče indexu?

### Odpověď (Back)

Je to pomocná struktura umožňující rychlý přístup k datům podle klíče indexu.
**Selektivita **(kardinalita) **klíče **se získá jako \(\frac{\#\text{různých hodnot}}{\#\text{řádků tabulky}}\)
**Typy:**

- indexy založené na struktuře B-stromu (vysoká selektivita - blízko 1)
- bitmapové indexy (velmi nízká selektivita)

## Poznámka Anki 1651510223713

Karty Anki: 1651510223713
GUID: mGwMo/)e>L; štítky: bi-dbs::p11.

Metadata původního zdroje pro kartu 1651510223713: v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to OLTP? Jaký typ indexu používá?

### Odpověď (Back)

Online Transaction Processing znamená, že s databází pracuje velké množství uživatelů, vykonávají malé transakce a přístupují náhodně. Používá B-stromové indexy.

## Poznámka Anki 1651510309246

Karty Anki: 1651510309246
GUID: o?fW7X7Uu{; štítky: bi-dbs::p11.

Metadata původního zdroje pro kartu 1651510309246: v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to DSS a OLAP? Jaké typy indexů používají?

### Odpověď (Back)

- **DSS** - Decision Support Systems
- **OLAP** - Online Analytical Processing
Používají bitmapové indexy.

