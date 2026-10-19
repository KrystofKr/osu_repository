# BI-OSY – Přednáška 11

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-osy/BI-OSY.apkg; APKG SHA-256 e601d54cae58e1923ab743a64796ef89ec49f6bcd52ac062288890242af207fc. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: b95b42cacacaa5de70f8162d09b00582086c2fd5b59f3a299e3fc9531a688ab6.
Původní balíčky: BI-OSY
Rozsah: 7 poznámek, 7 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1683118045099

Karty Anki: 1683118045099
GUID: A!@6[(+LA; štítky: bi-ib::02 bi-osy::p11.

### Otázka (Front)

Popište rozložení dat na disku.

### Odpověď (Back)

Disk je typicky rozdělen na následující části:

- **disk label** - obsahuje partition table a bootloader,

- **diskové oblasti** - partitions nebo slices.

## Poznámka Anki 1683118267904

Karty Anki: 1683118267904
GUID: HR(znDXa+4; štítky: bi-ib::02 bi-osy::p11.

### Otázka (Front)

Popište rozložení dat ve FS.

### Odpověď (Back)

V oblasti disku, ve které je vytvořen FS, existuje obvykle následující struktura:

- **bootblock** - kód sloužící pro zavedení OS,

- **superblock** - informace o konfiguraci FS (typ, velikost bloku, počet i-nodů, apod.)

- datové struktury pro **správu volného porstoru **(např. bitová mapa),
- datové struktury pro **uložení atributů souborů** (např. i-node tabulka),
- **datové bloky**.

## Poznámka Anki 1683119438900

Karty Anki: 1683119438900
GUID: Atcyr@}|2%; štítky: bi-ib::02 bi-ib::24 bi-osy::p11.

### Otázka (Front)

Popište File Allocation Table (FAT).

### Odpověď (Back)

File Allocation Table alokuje obsah souboru po jednotlivých datových blocích. Tabulka obsahuje tolik řádků, kolik je datových bloků ve FS. Soubor je reprezentován jako adresa prvního bloku. Každý řádek tabulky pak obsahuje jednu z následujících hodnot:

- **free** - datový blok je volný;

- **adresa** - adresa následujícího bloku, kde pokračuje obsah souboru;

- \(\mathtt{EOF}\) (konec zřetězení) - blok je posledním blokem souboru.

## Poznámka Anki 1683120021323

Karty Anki: 1683120021323
GUID: I5WPi)c=O~; štítky: bi-ib::02 bi-osy::p11.

### Otázka (Front)

Popište i-node.

### Odpověď (Back)

I-node (index node) je datová struktura, která má fixní velikost. Obsahuje atributy souboru nebo adresáře a adresy datových bloků, kde je uložen jeho obsah. Konkrétně jeho obsah vypadá následovně:

- 12 **přímých adres** ukazujících přímo na datové bloky s obsahem souboru;
- 1** nepřímá adresa první úrovně** ukazující na blok, ve kterém jsou přímé adresy;

- 1 **nepřímá adresa druhé úrovně** ukazující na blok, ve kterém jsou nepřímé adresy první úrovně;
- 1 **nepřímá adresa třetí úrovně** ukazující na blok, ve kterém jsou nepřímé adresy druhé úrovně.

 [Obrázek: paste-e8b437d03042c4e288e3bbb685573e34cdd0cfdf.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1683120310810

Karty Anki: 1683120310810
GUID: Cavmb4k3;y; štítky: bi-ib::02 bi-osy::p11.

Metadata původního zdroje pro kartu 1683120310810: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište implementaci adresáře ve FS.

### Odpověď (Back)

Obsah adresáře je stejně jako obsah souboru uložen v jednom nebo několika datových blocích. Z hlediska implementace rozlišujeme dva přístupy:

- adresář obsahuje **většinu informací** (jména, atributy a odkazy na bloky souborů a podadresářů),
- adresář obsahuje **minimum informací **(jméno a odkaz do speciální datové struktury, např. i-node tabulky).

## Poznámka Anki 1683120397200

Karty Anki: 1683120397200
GUID: L^u5[AQo&^; štítky: bi-ib::02 bi-osy::p11.

### Otázka (Front)

Popište implementaci odkazů ve filesystému.

### Odpověď (Back)

Existují dvě implementace odkazu ve filesystému:

- **soft link** - implementován pomocí cesty k souboru,

- **hard link** - implementován pomocí odkazu na speciální datovou strukturu, např. i-node.

## Poznámka Anki 1687812781046

Karty Anki: 1687812781046
GUID: IyH-86ErC-; štítky: bi-osy::p11.

Metadata původního zdroje pro kartu 1687812781046: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Jaké jsou možné způsoby implementace filesystému?

### Odpověď (Back)

Existují následující způsoby implementace filesystému podle metod alokace datových bloků:

- **alokace souboru pomocí souvislých oblastí datových bloků** (VxFS),
- **alokace souboru po jednotlivých datových blocích**:

- pomocí tabulky (FAT),
- pomocí i-nodů (UFS).

