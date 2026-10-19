# BI-OSY – Přednáška 07

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-osy/BI-OSY.apkg; APKG SHA-256 e601d54cae58e1923ab743a64796ef89ec49f6bcd52ac062288890242af207fc. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: b95b42cacacaa5de70f8162d09b00582086c2fd5b59f3a299e3fc9531a688ab6.
Původní balíčky: BI-OSY
Rozsah: 7 poznámek, 7 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1680700918437

Karty Anki: 1680700918438
GUID: QVzY;G>XSE; štítky: bi-ib::03 bi-ib::06 bi-osy::p07 bi-spol::18.

### Otázka (Front)

Co je to virtuální adresní prostor (VAS) a jaké obsahuje struktury?

### Odpověď (Back)

Virtuální adresní prostor je rozpětí virtuálních adres, které jsou poskytovány procesům operačním systémem. Tento adresní prostor se mapuje do fyzické paměti. Bězně obsahuje následující sekce:

- **program** (\(\mathtt{TEXT}\)),

- **globální proměnné **(\(\mathtt{DATA}\)),

- **halda** (heap space),

- **knihovny** (libraries),

- **zásobník nebo zásobníky** (stack space).

## Poznámka Anki 1680701207284

Karty Anki: 1680701207284
GUID: E/&[R~qzQK; štítky: bi-ib::03 bi-ib::06 bi-osy::p07 bi-spol::18.

Metadata původního zdroje pro kartu 1680701207284: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište virtuální adresní prostor identický s fyzickou pamětí.

### Odpověď (Back)

VAS identický s fyzickou pamětí je nejjednodušší implementace virtuálního adresního prostoru. V paměti se nachází pouze OS a jeden uživatelský proces, který je nahrán vždy od stejné adresy.

## Poznámka Anki 1680701341905

Karty Anki: 1680701341905
GUID: KybDv_MA%.; štítky: bi-ib::03 bi-ib::06 bi-osy::p07 bi-spol::18.

Metadata původního zdroje pro kartu 1680701341905: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište VAS s dynamickými oblastmi.

### Odpověď (Back)

VAS je mapován do fyzické paměti jako jedna souvislá oblast. V paměti se nachází OS a několik uživatelských procesů. Nastává ale problém s fragmentací, neboť končící programy zanechávají mezery v paměti. Řešením je stránkování.

 [Obrázek: paste-f516d2ee8ed29d646246251f1926c7a18f661d40.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1680702235555

Karty Anki: 1680702235556
GUID: fY]Czw2Rsg; štítky: bi-ib::03 bi-osy::p07 bi-spol::18.

Metadata původního zdroje pro kartu 1680702235556: v původním balíčku pozastavená karta.

### Otázka (Front)

Jaké existují způsoby zavedení programu do paměti?

### Odpověď (Back)

Existují následující přístupy:

- **absolutní zavedení **(absolute loading) - odkazy v programu obsahují absolutní adresy;

- **přemístitelné zavedení **(relocatable loading) - odkazy v programu obsahují relativní adresy, které přepočítá loader;
- **dynamic run-time loading **- odkazy v programu obsahují relativní adresy, které se při přístupu přepočtou pomocí MMU.

## Poznámka Anki 1687707997923

Karty Anki: 1687707997923
GUID: rehA,SfvYd; štítky: bi-osy::p07.

Metadata původního zdroje pro kartu 1687707997923: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte skrytou paměť (cache).

### Odpověď (Back)

Skrytá paměť je uživatelskému programu neviditelná paměť, kterou používá runtime systém pro ukládání opakovaně použtých dat nebo instrukcí blíže procesoru. Bývá integrována uvnitř procesoru a realizována pomocí SRAM.

## Poznámka Anki 1687708171472

Karty Anki: 1687708171472
GUID: e>E(sjp#|;; štítky: bi-osy::p07.

Metadata původního zdroje pro kartu 1687708171472: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Popište princip časové a prostorové lokality.

### Odpověď (Back)

**Princip časové lokality** říká, že data, ke kterým bylo přistupováno nedávno, budou opět brzy používána. **Princip prostorové lokality **tvrdí, že k datům v okolí těch dat, která jsou aktuálně používána, budou brzo brzy také přistupováno.

## Poznámka Anki 1716673897609

Karty Anki: 1716673897609
GUID: i1Eq^o>22T; štítky: bi-ib::08 bi-osy::p07 bi-spol::18.

Metadata původního zdroje pro kartu 1716673897609: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište metody správy volné paměti virtuálních adresních prostorů.

### Odpověď (Back)

Existují následující přístupy ke správě volné paměti virtuálních adresních prostorů:

- **bitová mapa** - paměť je rozdělena na alokační jednotky stejné velikosti, pro každou z nich obsahuje bitová mapa jeden bit;

- **zřetězené seznamy** - volné alokační jednotky jsou sdružovány v několika seznamech, každý z nich obsahuje pouze jednotky daných velikostí;

- **buddy systém** - stejný princip jako zřetězené seznamy, ale alokační jednotky mají velikosti mocnin dvou, což umožňuje rychlejší slučování jednotek při dealokaci paměti.

