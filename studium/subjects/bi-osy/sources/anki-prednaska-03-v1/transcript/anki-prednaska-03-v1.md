# BI-OSY – Přednáška 03

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-osy/BI-OSY.apkg; APKG SHA-256 e601d54cae58e1923ab743a64796ef89ec49f6bcd52ac062288890242af207fc. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: b95b42cacacaa5de70f8162d09b00582086c2fd5b59f3a299e3fc9531a688ab6.
Původní balíčky: BI-OSY
Rozsah: 14 poznámek, 14 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1678282577972

Karty Anki: 1678282577973
GUID: G]ltLf6Gb(; štítky: bi-osy::p03 bi-spol::17.

### Otázka (Front)

Co je to uváznutí (deadlock)?

### Odpověď (Back)

Uváznutí je situace, kdy několik vláken čeká na událost, kterou může vyvolat pouze jedno z čekajících vláken.

## Poznámka Anki 1678282615941

Karty Anki: 1678282615941
GUID: H$zuEO-Hvm; štítky: bi-osy::p03.

### Otázka (Front)

Co je to livelock?

### Odpověď (Back)

Livelock je situace, kdy několik vláken vykonává neužitečný výpočet, ale nemohou dosáhnout cílového stavu.

## Poznámka Anki 1678282652079

Karty Anki: 1678282652079
GUID: Ew9i6jpGFr; štítky: bi-osy::p03 bi-spol::17.

### Otázka (Front)

Co je to hladovění (starvation)?

### Odpověď (Back)

Hladovění je situace, kdy je vlákno ve stavu ready předbíháno a po dlouhou dobu mu nejsou přiděleny prostředky.

## Poznámka Anki 1678283032974

Karty Anki: 1678283032974
GUID: l/lUl5dnJ1; štítky: bi-osy::p03 bi-spol::17.

### Otázka (Front)

Jak lze docílit synchronizace kritické sekce?

### Odpověď (Back)

Buď pomocí **aktivního čekání** nebo pomocí **blokujících systémových volání či knihovních funkcí**.

## Poznámka Anki 1678283136302

Karty Anki: 1678283136302
GUID: fst*foJNcd; štítky: bi-osy::p03 bi-spol::17.

### Otázka (Front)

Popište synchronizaci kritické sekce pomocí aktivního čekání.

### Odpověď (Back)

Aktivní čekání je způsob synchronizace krytické sekce. Stav kritické sekce je uchováván ve sdílené proměnné a před vstupem do kritické sekce je vláknem **aktivně** testována (např. pomocí \(\mathtt{test\text-and\text-set}\)) dokud se sekce neuvolní. Při vstupu a opouštění kritické sekce vlákno proměnnou patřičně upraví.

## Poznámka Anki 1678284383281

Karty Anki: 1678284383281
GUID: Jqg<H{8F)(; štítky: bi-osy::p03 bi-spol::17.

Metadata původního zdroje pro kartu 1678284383281: v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to inverzní prioritní problém?

### Odpověď (Back)

Předpokládejme:

- plánování vláken s fixní prioritou,
- omezený počet jader,
- synchronizaci aktivním čekáním.

Uváznutí nastane, pokud:

- vlákno \(A\) má nízkou prioritu a nachází se v kritické sekci,
- vlákno \(B\) má vyšší prioritu a čeká na vstup,
- všechna jádra jsou obsazena vlákny s vyšší prioritou.

## Poznámka Anki 1678284700553

Karty Anki: 1678284700553
GUID: zrmP4}|h-N; štítky: bi-osy::p03 bi-spol::17.

### Otázka (Front)

Popište synchronizaci kritické sekce pomocí blokujícího systémového volání či knihovní funkce.

### Odpověď (Back)

Synchronizace pomocí blokujícího volání či knihovní funkce je implementováno pomocí datových struktur, které umožňují:

- pamatovat si stav kritické sekce,
- udržovat seznam vláken čekajících na vstup do kritické sekce.

Před vstupem do kritické sekce vlákno provede systémové volání či knihovní funkci a v případě:

- **zamčené sekce** přejde vlákno do stavu blocked a pasivně čeká,

- **odemčené sekce** kritickou sekci zamkne a vstoupí do ní (později ji zase odemkne).

## Poznámka Anki 1678285101039

Karty Anki: 1678285101039
GUID: rt@(~k!]a1; štítky: bi-osy::p03 bi-spol::17.

Metadata původního zdroje pro kartu 1678285101039: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište problém producent-konzument?

### Odpověď (Back)

Problém producent-konzument je synchronizační problém, kdy si několik vláken vyměňuje data přostřednictvím sdílené paměti s omezenou velikostí. **Producent** data do fronty vkládá a **konzument** data z fronty vybírá. Vznikají následující problémy:

- je nutné zajistit výlučný přístup při vkládání a vybírání,
- pokud je fronta prázdná, je nutné zablokovat konzumenta,
- pokud je fronta plná, je nutné zablokovat producenta.

## Poznámka Anki 1687706324600

Karty Anki: 1687706324601
GUID: hMv{hj=#aZ; štítky: bi-osy::p03.

Metadata původního zdroje pro kartu 1687706324601: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Popište sémantiku instrukce \(\mathtt{test \text- and \text- set}\).

### Odpověď (Back)

Instukce \(\mathtt{test \text- and \text- set}\) je atomická instrukce, která se používá k implementaci zámků pro vzájemné vyloučení. Pracuje nad sdílenou proměnnou \(Z\), kde

- \(Z = 0\) znamená, že kritická sekce je uvolněná,

- \(Z = 1\) znamená, že kritická sekce je obsazená.

Při volání \(\mathtt{test \text- and \text- set}\) je do \(Z\) zapsána \(\mathtt 1\), ale vrácena její hodnota před změnou. V případě, že instrukce vrátí \(\mathtt 0\), pak byl zámek získán, v opačném případě nikoliv.

## Poznámka Anki 1716661538424

Karty Anki: 1716661538425
GUID: nV}K<Z>%;p; štítky: bi-osy::p03 bi-spol::17.

Metadata původního zdroje pro kartu 1716661538425: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište problém večeřících filosofů.

### Odpověď (Back)

Problém večeřících filosofů je synchronizační problém. Kolem stolu sedí \(n\) filosofů, před každým z nich se nachází talíř a mezi každými sousedícími talíři leží jedna vidlička. Pokud chce filosof večeřet, musí získat obě vidličky, které leží nalevo a napravo od jeho talíře. Cílem je zajistit, aby najednou mohlo večeřet \(\lfloor \frac n 2 \rfloor\) filosofů.

## Poznámka Anki 1716661778011

Karty Anki: 1716661778011
GUID: J3:Fp#/hNl; štítky: bi-osy::p03 bi-spol::17.

Metadata původního zdroje pro kartu 1716661778011: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište problém čtenářů a písařů.

### Odpověď (Back)

Problém čtenářů a písařů je synchronizační problém. Uvažujme několik čtenářů, kteří chtějí používat sdílený prostředek pouze pro čtení, a několik písařů, kteří chtějí sdílený prostředek modifikovat. Cílem je zajistit, aby pouze jeden písař mohl modifikovat obsah prostředku v jednom okamžiku a v případě, že žádný písař k prostředku nepřistupuje, povolit čtenářům prostředek číst. Řešení by také mělo být spravedlivé, tedy pokud čtenář nebo písař čeká na sdílený prostředek, neměl by ho žádný jiný čtenář nebo písař předběhnout.

## Poznámka Anki 1716662060688

Karty Anki: 1716662060688
GUID: xlSjeG5or@; štítky: bi-osy::p03 bi-spol::17.

Metadata původního zdroje pro kartu 1716662060688: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište problém spících holičů.

### Odpověď (Back)

Problém spících holičů je synchronizační problém. Uvažujme holičství s \(n\) holiči, \(n\) křesly k holení a \(m\) křesly k čekání. Pokud není žádný zákazník v holičství, holič usne. Pokud přijde zákazník, mohou nastat tři situace:

- pokud existuje volný holič, zákazník se nechá ostříhat;
- pokud neexistuje volný holič, ale je volné křeslo k čekání, zákazník počká;
- jinak zákazník opustí holičství.

Cílem je zajistit, aby pracoval co možná nejvyšší počet holičů.

## Poznámka Anki 1716662224582

Karty Anki: 1716662224582
GUID: Q!SVg]9X?R; štítky: bi-osy::p03 bi-spol::17.

Metadata původního zdroje pro kartu 1716662224582: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište typy vláken z hlediska jejich plánování.

### Odpověď (Back)

Z hlediska plánování rozlišuje operační systém tři typy vláken:

- **CPU orientovaná vlákna** - využívá CPU po delší dobu, vyvolává méně blokujících operací;
- **I/O orientovaná vlákna** - využívá CPU po kratší dobu, vyvolává více blokujících operací;
- **real-time vlákna** - musí zareagovat na událost během daného intervalu.

## Poznámka Anki 1716662547076

Karty Anki: 1716662547076
GUID: vx!Ing:piC; štítky: bi-osy::p03 bi-spol::17.

Metadata původního zdroje pro kartu 1716662547076: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište způsoby zotavení z uváznutí (deadlock) vláken.

### Odpověď (Back)

Uváznutí (deadlock) vláken lze řešit následujícími přístupy:

- současné ukončení všech uvázlých vláken,
- postupné ukončování uvázlých vláken,
- obnovení předchozího stavu vláken.

