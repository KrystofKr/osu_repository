# BI-BEK – Přednáška 02

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-bek/BI-BEK.apkg; APKG SHA-256 8b1a9f700cf93cf99c030811606998d3d282ec99cc7d73e806af320f264d4ea6. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 735709f33719335ca8dfc56a2c567cb9b621f1f50f3818756a9e3f4fd0fc9380.
Původní balíčky: BI-BEK
Rozsah: 14 poznámek, 14 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1678289067361

Karty Anki: 1678289067361
GUID: e)5AHwCFo]; štítky: bi-bek::p02 bi-spol::19.

### Otázka (Front)

Co je role preprocesoru?

### Odpověď (Back)

Preprocesor vyhodnocuje direktivy (např. \(\mathtt{\#include}\)) a nahradí je. Výsledek předává překladači.

## Poznámka Anki 1678289425293

Karty Anki: 1678289425293
GUID: LiIGTYx}A&; štítky: bi-bek::p02 bi-spol::19.

### Otázka (Front)

Co je role překladače?

### Odpověď (Back)

Překladač (kompilátor) čte tokeny z preprocesovaného zdrojového souboru, kontroluje syntaxi a hlásí varování nebo chyby. Následně zdrojový kód transformuje do vnitřní reprezentace a optimalizuje ji. Výsledkem je strojový kód ve formě objektového souboru.

## Poznámka Anki 1678290727007

Karty Anki: 1678290727008
GUID: f2N0;>5IZ1; štítky: bi-bek::p02.

### Otázka (Front)

Co obsahuje sekce \(\mathtt{\text.bss}\) objektového souboru?

### Odpověď (Back)

\(\mathtt{\text.bss}\) (block started by symbol) obsahuje data, která jsou inicializovaná na nulu.

## Poznámka Anki 1678290833534

Karty Anki: 1678290833534
GUID: wNp:l@O/G-; štítky: bi-bek::p02.

### Otázka (Front)

Co obsahuje sekce \(\mathtt{\text.drectve}\) objektového souboru?

### Odpověď (Back)

Obsahuje řetězec direktiv pro linker.

## Poznámka Anki 1678290966634

Karty Anki: 1678290966634
GUID: c3m>CL?B_=; štítky: bi-bek::p02.

### Otázka (Front)

Co obsahuje sekce \(\mathtt{\text.data}\) objektového souboru? Jaký je její vztak k sekcím \(\texttt{.rdata}\) a \(\texttt{.text}\)?

### Odpověď (Back)

Obsahuje inicializovaná (nenulová) data. Data pouze pro čtení se mapují do sekcí \(\mathtt{\text.rdata}\) nebo \(\mathtt{\text.text}\).

## Poznámka Anki 1678291503000

Karty Anki: 1678291503000
GUID: yjL@5@;#e]; štítky: bi-bek::p02.

### Otázka (Front)

Co obsahuje sekce \(\mathtt{\text.debug}\) objektového souboru?

### Odpověď (Back)

Obsahuje informace překladače pro ladění.

## Poznámka Anki 1678291618924

Karty Anki: 1678291618924
GUID: Q6~k06}L{&; štítky: bi-bek::p02.

### Otázka (Front)

Co obsahuje sekce \(\mathtt{\text.text}\) objektového souboru?

### Odpověď (Back)

Obsahuje spustitelný kód. Typicky je spustitelná a jen pro čtení.

## Poznámka Anki 1678292239505

Karty Anki: 1678292239505
GUID: Q733Bj@c4G; štítky: bi-bek::p02.

### Otázka (Front)

K čemu slouží relokační tabulka v objektovém souboru? Na jakých jiných strukturách závisí?

### Odpověď (Back)

Obsahuje informace o tom, jak patřičnou sekci upravit před jejím nahráním do paměti. Používá k tomu tabulku symbolů.

## Poznámka Anki 1678292509273

Karty Anki: 1678292509273
GUID: s@fWxMEBJH; štítky: bi-bek::p02 ni-pb::12.

### Otázka (Front)

Co je to dekorace jmen (name mangling)?

### Odpověď (Back)

Dekorace jmen (name mangling) je proces zanášení dodatečné informace do jména symbolu, čímž vznikají unikátní pojmenování symbolů.

## Poznámka Anki 1678292873188

Karty Anki: 1678292873189
GUID: tS)vZ(_&|Q; štítky: bi-bek::p02 bi-ib::08 bi-spol::19.

### Otázka (Front)

Co je to statická knihovna? Jaké rozlišujeme typy?

### Odpověď (Back)

Statická knihovna je kolekce objektových souborů. Kopie statické knihovny je při linkování přípojena k výslednému programu. Rozlišujeme:

- **archivní **- obsahuje kód a data, která jsou připojeny k programu;

- **importní**** **- obsahuje pseudo-objektové soubory, které umoňují najít a připojit dynamickou knihovnu k programu.

## Poznámka Anki 1678292912653

Karty Anki: 1678292912653
GUID: swXUv~k_>; štítky: bi-bek::p02 bi-ib::08 bi-spol::19.

### Otázka (Front)

Jak funguje dynamická knihovna?

### Odpověď (Back)

Dynamická knihovna je dohledána a připojena k programu až při jeho spuštění.

## Poznámka Anki 1678293444103

Karty Anki: 1678293444103
GUID: n./W,{}@)D; štítky: bi-bek::p02.

### Otázka (Front)

Popište importní adresář (import directory table).

### Odpověď (Back)

Importní adresář (import directory table) se nachází v sekci \(\texttt{.idata}\) a je tvořen strukturami \(\texttt{IMAGE_IMPORT_DESCRIPTOR}\). Každá z těchto struktur popisuje jedno DLL, ze kterého jsou importovány symboly, a obsahuje, mimo jiné, ukazatel na Import Address Table (IAT).

## Poznámka Anki 1678293692573

Karty Anki: 1678293692573
GUID: fp=klBI~qo; štítky: bi-bek::p02.

### Otázka (Front)

Co je to exportní tabulka?

### Odpověď (Back)

Exportní tabulka obsahuje symboly knihovny určené pro exportování. Díky tomu může být knihovna dynamicky linkována ostatními programy.

## Poznámka Anki 1678293881450

Karty Anki: 1678293881450
GUID: CdeJn:iNQW; štítky: bi-bek::p02 bi-spol::19.

### Otázka (Front)

Co je to sestavování (linking)? Z jakých se skládá fází?

### Odpověď (Back)

Sestavování (linking) je proces, při kterém se objektové soubory, statické knihovny a importní knihovny kombinují ve spustitelný soubor nebo dynamickou knihovnu. Probíhá ve dvou fázích:

- **budování tabulky symbolů** - linker přečte tabulky symbolů vstupních souborů a vytvoří jednu společnou,

- **relokace** - linker doplní do kódu odkazy na data, které lze ze společné tabulky symbolů vyplnit.

