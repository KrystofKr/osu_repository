# BI-ADU – Přednáška 06

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-adu/BI-ADU.apkg; APKG SHA-256 82e24d30673cd0e7a3a5aa4e190d583b7bbdacb9961363822343a47e911816b0. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: e4dcf13ba19280a57f78abe30db474a9b8da6ee148ccef4aa2c510acfc892435.
Původní balíčky: BI-ADU
Rozsah: 5 poznámek, 5 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1680077502990

Karty Anki: 1680077502990
GUID: K{~ME:9fi<; štítky: bi-adu::p06 bi-ib::02.

Metadata původního zdroje pro kartu 1680077502990: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište princip Zettabyte File System (ZFS).

### Odpověď (Back)

Zettabyte File System používá stejné technologie jako UFS (i-node tabulka, atributy, odkazy, apod.), ale má odlišnou implementaci. Datový prostor tvoří virtuální datová oblast **pool**, která se skládá z jednotlivých zdrojů dat - **disků**, **partitions** (slices) a **souborů** (virtuálních zařízení). Z poolu se potom alokují jednotlivé **datové bloky**. Každý blok má ve svém nadřazeném datovém bloku kontrolní součet. Nad bloky je sestaven **vyhledávací strom**. ZFS používá transakční systém a **copy-on-write **a umí automaticky **detekovat i opravit chyby**.

 [Obrázek: paste-f90e40ee2f8a8e94d0311865735f3f3a2c47b004.jpg; soubor je v media/ v doprovodném ZIP] 

 [Obrázek: paste-ba6d940937874ebc9586dda4fa120f58b4fdcca0.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1680080750670

Karty Anki: 1680080750670
GUID: v_EPee(?ii; štítky: bi-adu::p06 bi-ib::02.

Metadata původního zdroje pro kartu 1680080750670: v původním balíčku pozastavená karta.

### Otázka (Front)

Jaké existují typy Zettabyte File System poolů?

### Odpověď (Back)

Existují následující typy poolů:

- standalone (non-redundant) - princip stripe,
- mirrored,
- RAID-Z.

## Poznámka Anki 1680080852804

Karty Anki: 1680080852805
GUID: kaVT0%~I_-; štítky: bi-adu::p06 bi-ib::02.

Metadata původního zdroje pro kartu 1680080852805: v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to RAID-Z?

### Odpověď (Back)

RAID-Z je nestandartní RAID verze používaná na Zettabyte File System. Staví na RAID 5 (stripe po blocích, distribuovaná parita), ale používá dynamickou šířku stripe. Každý blok má svůj vlastní stripe, čímž je dosaženo atomicity operací (full-stripe write).

## Poznámka Anki 1683810617649

Karty Anki: 1683810617649
GUID: pSP4j-XL5=; štítky: bi-adu::p06 bi-ib::02.

Metadata původního zdroje pro kartu 1683810617649: v původním balíčku pozastavená karta.

### Otázka (Front)

Jakou diskovou kapacitu potřebujeme pro snapshot?

### Odpověď (Back)

Disková kapacita nutná pro snapshot se bude odvíjet od dvou parametrů - velikost snapshotovaného zařízení a početu změn provedených od posledního snapshotu. To proto, že snapshoty nevytvářejí identické kopie, ale spíše sledují změny oproti předchozí verzi. Toho se např. v Zettabyte File System dosahuje pomocí copy-on-write.

## Poznámka Anki 1684330935131

Karty Anki: 1684330935132
GUID: x}<,*Mm*Z4; štítky: bi-adu::p06 bi-ib::02.

Metadata původního zdroje pro kartu 1684330935132: v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to self-healing u Zettabyte File System?

### Odpověď (Back)

Self-healing je funkce Zettabyte File System, díky které použitím CRC a RAID dokáže filesystém sám detekovat a opravit chybu.

