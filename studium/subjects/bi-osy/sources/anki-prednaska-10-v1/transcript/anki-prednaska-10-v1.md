# BI-OSY – Přednáška 10

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-osy/BI-OSY.apkg; APKG SHA-256 e601d54cae58e1923ab743a64796ef89ec49f6bcd52ac062288890242af207fc. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: b95b42cacacaa5de70f8162d09b00582086c2fd5b59f3a299e3fc9531a688ab6.
Původní balíčky: BI-OSY
Rozsah: 9 poznámek, 9 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1682512934346

Karty Anki: 1682512934346
GUID: I)i;k9P&!L; štítky: bi-ib::02 bi-osy::p10.

Metadata původního zdroje pro kartu 1682512934346: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište architekturu HDD.

### Odpověď (Back)

HDD (hard disk drive) se skládá z mechanických částí:

- **plotny **- mají vždy dva povrchy a otáčí se stejnou rychlostí,
- **hlavičky **- umožňují čtení a zápis na příslušný povrch;

a elektrických částí:

- **řadič disku** - obsahuje procesor, paměť, firmware,

- **vyrovnávací paměť** - DRAM.

## Poznámka Anki 1682513144372

Karty Anki: 1682513144372
GUID: Jg*]~7,c4b; štítky: bi-ib::02 bi-osy::p10.

### Otázka (Front)

Co je to sektor, stopa a cylindr na HDD?

### Odpověď (Back)

**Sektor **je nejměnší adresovatelná jednotka na disku (dříve 512 B, nyní 4096 B). **Stopa** je množina sektorů na jednom povrchu ve stejné vzdálenosti od středu. **Cylindr** je množina všech stop o daném poloměru na všech površích.

 [Obrázek: paste-7ee70403c7e05b812fdde3255175be218c9eba09.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1682514996651

Karty Anki: 1682514996651
GUID: r:b/{u<m8b; štítky: bi-ib::02 bi-osy::p10.

Metadata původního zdroje pro kartu 1682514996651: v původním balíčku pozastavená karta.

### Otázka (Front)

Na čem závisí rychlost čtení a zápisu jednoho sektoru HDD?

### Odpověď (Back)

Rychlost čtení a zápisu sektoru závisí na následujících faktorech:

- **doba vystavení** (seek time) - čas nastavení hlaviček na správný cylindr,

- **průměrné rotační zpoždění **(rotational delay) - čas posunutí správného sektoru pod hlavičku,

- **čas přenosu dat**.

## Poznámka Anki 1682515165594

Karty Anki: 1682515165594
GUID: geck.71M=j; štítky: bi-ib::02 bi-osy::p10.

Metadata původního zdroje pro kartu 1682515165594: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište first-in, first-out (FIFO) algoritmus plánování přístupu k HDD.

### Odpověď (Back)

Požadavky jsou obslouženy v tom pořadí, v jakém přišly. Tento algoritmus je spravedlivý, ale poskytuje horší výkon.

## Poznámka Anki 1682515260250

Karty Anki: 1682515260250
GUID: i_jr)O?{7e; štítky: bi-ib::02 bi-osy::p10.

Metadata původního zdroje pro kartu 1682515260250: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište shortest service time first (SSTF) algoritmus plánování přístupu k HDD.

### Odpověď (Back)

Nejdříve jsou obslouženy požadavky, které vyžadují nejmenší pohyb hlaviček z aktuální pozice. Poskytuje lepší výkon než FIFO, ale hlavičky mají tendenci setrvávat uprostřed disku.

## Poznámka Anki 1682515331554

Karty Anki: 1682515331554
GUID: g:jSqsjx$S; štítky: bi-ib::02 bi-osy::p10.

Metadata původního zdroje pro kartu 1682515331554: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište SCAN algoritmus (elevator algorithm) plánování přístupu k HDD.

### Odpověď (Back)

Hlavičky se pohybují tak, aby nejdříve byly obslouženy požadavky v jednom směru. Poté se směr pohybu může změnit. Omezuje problém stárnutí požadavků, ale poskytuje horší výkon než SSTF.

## Poznámka Anki 1682515430611

Karty Anki: 1682515430611
GUID: xu2fN}jc(+; štítky: bi-ib::02 bi-osy::p10.

Metadata původního zdroje pro kartu 1682515430611: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište \(N\)-Step-SCAN algoritmus plánování přístupu k HDD.

### Odpověď (Back)

\(N\)-Step-SCAN algoritmus je vylepšená verze SCAN algoritmu, kdy jsou požadavky sdružovány do několika front délky \(N\). Fronty jsou postupně obsluhovány pomocí SCAN algoritmu.

## Poznámka Anki 1682516386275

Karty Anki: 1682516386275
GUID: hO=:)5@r?i; štítky: bi-osy::p10.

Metadata původního zdroje pro kartu 1682516386275: v původním balíčku pozastavená karta.

### Otázka (Front)

Jak rozišujeme datová úložiště podle způsobu připojení?

### Odpověď (Back)

Datová úložiště dle způsobu připojení rozdělíme na:

- **DAS** (direct-attached storage) - připojení přímo přes I/O porty systému,

- **NAS** (network-attached storage) - připojení pomocí síťových protokolů,

- **SAN** (storage area network) - datová úložiště jsou v oddělené síti.

## Poznámka Anki 1687811855513

Karty Anki: 1687811855513
GUID: NWgKo?97IK; štítky: bi-osy::p10.

Metadata původního zdroje pro kartu 1687811855513: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Popište redundant array of independent disks (RAID) a jeho verze.

### Odpověď (Back)

RAID (redundant array of independent disks) je řešení, které kombinuje vícero disků do jednoho virtuálního a poskytuje výhody jako zvýšení kapacity, bezpečnosti nebo výkonu. Existují následující verze RAID:

- **RAID 0** (skládání):

- concatenation - disky jsou řazeny za sebe,

- striping - disky jsou řazeny vedle sebe,

- **RAID 1** (zrcadlení);

- **RAID 0+1 **a **RAID 1+0 **(kombinace stripe a mirror nebo mirror a stripe);

- **RAID 2** (stripe po bitech, Hammingův kód);

- **RAID 3 **(stripe po bytech, dedikovaný paritní disk);

- **RAID 4 **(stripe po blocích, dedikovaný paritní disk);

- **RAID 5 **(stripe po blocích, distribuovaná parita);

- **RAID 6** (stripe po blocích, dvě distribuované parity).

