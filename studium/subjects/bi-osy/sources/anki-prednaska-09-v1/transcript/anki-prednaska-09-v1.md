# BI-OSY – Přednáška 09

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-osy/BI-OSY.apkg; APKG SHA-256 e601d54cae58e1923ab743a64796ef89ec49f6bcd52ac062288890242af207fc. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: b95b42cacacaa5de70f8162d09b00582086c2fd5b59f3a299e3fc9531a688ab6.
Původní balíčky: BI-OSY
Rozsah: 11 poznámek, 11 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1681908548727

Karty Anki: 1681908548727
GUID: k^`5_O~PSI; štítky: bi-ib::06 bi-osy::p09 bi-spol::18.

### Otázka (Front)

Popište segmentaci.

### Odpověď (Back)

Virtuální adresní prostor procesu je rozdělen na segmenty implementované pomocí dynamických oblastí. Logická adresa se dělí na segment selector a offset, přičemž segment selector se používá pro indexaci v **tabulce segmentů**. OS si pro každý proces udržuje jednu tabulku segmentů, čímž je docíleno oddělení adresních prostorů jednotlivých procesů. Vzniká však opět problém s fragmentací, která se řeší kombinací se stránkováním.

 [Obrázek: paste-7fdcbc572c917b2c2d45ccdd4bfc6d72fa77a6b2.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1681909186963

Karty Anki: 1681909186963
GUID: qeY[?IPTFm; štítky: bi-ib::06 bi-osy::p09 bi-spol::18.

Metadata původního zdroje pro kartu 1681909186963: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Popište strukturu jednoho řádku v tabulce segmentů.

### Odpověď (Back)

Tabulka segmentů obsahuje následující informace:

- **velikost segmentu** (length),
- **počáteční adresu segmentu** (base),
- ****řídící **bity**.

## Poznámka Anki 1681910513941

Karty Anki: 1681910513941
GUID: t1=<kiO*67; štítky: bi-ib::06 bi-osy::p09 bi-spol::18.

Metadata původního zdroje pro kartu 1681910513941: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište optimální algoritmus pro náhradu stránek.

### Odpověď (Back)

Optimální algoritmus nahradí tu stránku, která má čas příštího přístupu nejdelší. Algoritmus je v praxi nevyužitelný, protože nelze předpovídat budoucnost.

## Poznámka Anki 1681910913421

Karty Anki: 1681910913421
GUID: Iv&ieOJJ&A; štítky: bi-ib::06 bi-osy::p09 bi-spol::18.

Metadata původního zdroje pro kartu 1681910913421: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište algoritmus not recently used (NRU) pro náhradu stránek.

### Odpověď (Back)

NRU (not recently used) využívá bity \(\mathtt{R}\) (reference) a \(\mathtt{M}\) (modified) a základě těchto bitů rozděluje stránky do čtyř tříd:

1. \(\mathtt R = 0\) a \(\mathtt M = 0\),

2. \(\mathtt R = 0\) a \(\mathtt M = 1\),
3. \(\mathtt R = 1\) a \(\mathtt M = 0\),

4. \(\mathtt R = 1 \) a \(\mathtt M = 1\),

přičemž stránky jsou do paměti zaváděny vždy s \(\mathtt R = 1\) a \(\mathtt R\) bit se periodicky  resetuje. NRU nahradí vždy stránku z neprázdné třídy s nejnižším číslem.

## Poznámka Anki 1681911066447

Karty Anki: 1681911066447
GUID: B$wE>lbNX?; štítky: bi-osy::p09.

Metadata původního zdroje pro kartu 1681911066447: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište algoritmus first-in, first-out pro náhradu stránek.

### Odpověď (Back)

OS si udržuje seznam všech stránek v hlavní paměti. Při nahrání stránky se její záznam zařadí na konec seznamu. Při nahrazování vybere FIFO první stránku z tohoto seznamu.

## Poznámka Anki 1681911576706

Karty Anki: 1681911576706
GUID: NKF%YAuRis; štítky: bi-ib::06 bi-osy::p09 bi-spol::18.

Metadata původního zdroje pro kartu 1681911576706: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište clock algoritmus pro náhradu stránek.

### Odpověď (Back)

Clock algoritmus je modifikovaný FIFO algoritmus. Seznam stránek je implementován jako kruhová fronta. Ukazatel (ručička) ukazuje na první položku fronty. Při nahrání stránky a každém přistupu se nastaví její \(\mathtt R\) (reference) bit na \(1\). Nahrazování probíhá tak, že ručička prochází buffer a pokud:

- narazí na stránku s \(\mathtt R = 1\), nastaví její \(\mathtt R\) na \(0\) a posune se,
- narazí na stránku s \(\mathtt R = 0\), bude nahrazena tato stránka.

## Poznámka Anki 1681911997118

Karty Anki: 1681911997118
GUID: C=2G[i10&E; štítky: bi-ib::06 bi-osy::p09 bi-spol::18.

Metadata původního zdroje pro kartu 1681911997118: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište two-handed clock algoritmus pro náhradu stránek.

### Odpověď (Back)

Two-handed clock algoritmus je vylepšený clock algoritmus se dvěma ručičkami. Opět pracuje s kruhovou frontou a při vkládání stránky nastavíme její \(\mathtt R\) (reference) bit na \(1\). První ručička resetuje \(\mathtt R\) na \(0\) a druhá označí stránku jako kandidáta na náhradu v případě, že její \(\mathtt R\) bit je nastaven na \(0\).

 [Obrázek: paste-10c363624d39e60379b7ecba771b4a3e0f43444e.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1681912227738

Karty Anki: 1681912227738
GUID: QzNC`v):NE; štítky: bi-ib::06 bi-osy::p09 bi-spol::18.

Metadata původního zdroje pro kartu 1681912227738: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište algoritmus least recently used (LRU) pro náhradu stránek.

### Odpověď (Back)

LRU (least recently used) vybere pro náhradu takovou stránku, ke které se nepřistupovalo po nejdelší dobu. Jeho implementace je složitá, místo něj se používá aging algoritmus.

## Poznámka Anki 1681912434052

Karty Anki: 1681912434052
GUID: ke|Yu*Z8nn; štítky: bi-osy::p09 bi-spol::18.

Metadata původního zdroje pro kartu 1681912434052: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište ageing algoritmus pro náhradu stránek.

### Odpověď (Back)

Společně s \(\mathtt R\) (reference) si OS pro každou stránku pamatuje ještě \(n\)-bitový čítač \(C\), který je při načtení stránky do paměti nastaven na samé jedničky. OS periodicky pro každou stránku

- posune \(C\) o jeden bit doprava,
- nastaví MSB \(C\) na hodnotu \(\mathtt R\),
- resetuje \(\mathtt R\) na nulu.

Vhodným kandidátem pro náhradu je pak stránka, jejíž čítač \(C\) má nejmenší hodnotu.

## Poznámka Anki 1687811014572

Karty Anki: 1687811014572
GUID: C=,4Rz]i56; štítky: bi-osy::p09.

Metadata původního zdroje pro kartu 1687811014572: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to demand paging (lazy loading)?

### Odpověď (Back)

Demand paging je strategie nahrávání stránek, při které je stránka nahrána do hlavní paměti až tehdy, když je k ní přistupováno. Toto mapování zajišťuje OS.

## Poznámka Anki 1687811135670

Karty Anki: 1687811135671
GUID: L.B0;Q:Ml~; štítky: bi-ib::06 bi-osy::p09 bi-spol::18.

Metadata původního zdroje pro kartu 1687811135671: v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to prepaging?

### Odpověď (Back)

Prepaging je strategie nahrávání stránek postavená na principu prostorové lokality. Funguje tak, že když proces přistupuje ke stránce, která ještě není v hlavní paměti, načte OS tuto stránku a několik následujících stránek.

