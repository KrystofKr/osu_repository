# BI-ADU – Přednáška 04

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-adu/BI-ADU.apkg; APKG SHA-256 82e24d30673cd0e7a3a5aa4e190d583b7bbdacb9961363822343a47e911816b0. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: e4dcf13ba19280a57f78abe30db474a9b8da6ee148ccef4aa2c510acfc892435.
Původní balíčky: BI-ADU
Rozsah: 9 poznámek, 9 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1678868252669

Karty Anki: 1678868252671
GUID: Gee10aOx$]; štítky: bi-adu::p04 bi-ib::02.

Metadata původního zdroje pro kartu 1678868252671: v původním balíčku pozastavená karta.

### Otázka (Front)

Jak jsou pospsána zařízení v Unixu?

### Odpověď (Back)

Zařízení jako disky, partitions, síťové karty, apod. jsou popsána pomocí speciálních souborů, pričemž operace nad těmito soubory znamenají operace nad daným zařízením.

## Poznámka Anki 1678868970687

Karty Anki: 1678868970687
GUID: El77#UB!$`; štítky: bi-adu::p04 bi-ib::02.

### Otázka (Front)

Popište speciální soubory. Kde je najdeme? Jaké rozlišujeme typy? Jak jsou popsány a implementovány?

### Odpověď (Back)

Speciální soubory jsou uloženy v \(\mathtt{/dev}\) a rozdělujeme je na

- **znakové** - raw, unbuffered,

- **blokové** - block, buffered.

Popsány jsou pomocí dvou čísel zařízení:

- **major** (velké) - driver,
- **minor** (malé) - parametr nebo instance.

Implementovány jsou pomocí metadat v i-node, která odkazují na driver do jádra, kterému jsou data předávána.

## Poznámka Anki 1678869631713

Karty Anki: 1678869631713
GUID: vUUZ(-F9Nm; štítky: bi-adu::p04 bi-ib::02.

Metadata původního zdroje pro kartu 1678869631713: v původním balíčku pozastavená karta.

### Otázka (Front)

Jak fungují disky v Solarisu a Linuxu?

### Odpověď (Back)

V Solarisu existují disky jako raw i jako block speciální soubory a každý disk má

- **logické jméno** - symbolický link na fyzické jméno (v adresáři \(\mathtt{/dev}\)),

- **fyzické jméno** - speciální soubor (v adresáři \(\mathtt{/devices}\)),

- **instanční jméno** - používané jádrem.

V Linuxu existují disky pouze pod fyzickým jménem v adresáři \(\mathtt{/dev}\) a typ přístupu (raw nebo block) vyplývá z jejich použití.

## Poznámka Anki 1678871212647

Karty Anki: 1678871212647
GUID: MGYSO=u.G2; štítky: bi-adu::p04 bi-ib::02.

Metadata původního zdroje pro kartu 1678871212647: v původním balíčku pozastavená karta.

### Otázka (Front)

Co obsahuje master boot record (MBR)? Jaká je jeho struktura?

### Odpověď (Back)

Master boot record obsahuje zavaděč OS a partition table. Jeho struktura je následující:

 [Obrázek: paste-24f24d66f0c30bd8bad83c097f931fe3236c3a6b.jpg; soubor je v media/ v doprovodném ZIP]

### Doplňující pole (Extra)

CHS označuje historické cylinder-head-sector adresování a LBA současný logical block addressing.

## Poznámka Anki 1678871396807

Karty Anki: 1678871396807
GUID: dC?CZ@,p48; štítky: bi-adu::p04 bi-ib::02.

Metadata původního zdroje pro kartu 1678871396807: v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to GUID Partition Table (GPT)? Jak se liší od master boot record a jakou má strukturu?

### Odpověď (Back)

GUID Partition Table je novější typ partition tabulky. Každé partition přiřazuje globálně unikátní identifikátor. Oproti MBR má možnosti obnovy - obsahuje CRC a zálohuje se na konci disku. Její struktura je následující:

 [Obrázek: paste-7bb9c09a1e0baeff7ac2528e0ee618f17b5cc887.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1678872305726

Karty Anki: 1678872305726
GUID: p,fYssFl=); štítky: bi-adu::p04 bi-ib::02.

Metadata původního zdroje pro kartu 1678872305726: v původním balíčku pozastavená karta.

### Otázka (Front)

Jaké jsou typy fyzických systémů souborů?

### Odpověď (Back)

Rozlišujeme následující typy systémů souborů:

- **diskové** (ext, NTFS, FAT32),

- **síťové **(NFS, Samba),

- **pseudo a paměťové filesystémy** (\(\mathtt{tmpfs}\), \(\mathtt{swapfs}\), \(\mathtt{procfs}\)).

## Poznámka Anki 1678872442965

Karty Anki: 1678872442965
GUID: m_]$?RZ|jA; štítky: bi-adu::p04 bi-ib::02.

Metadata původního zdroje pro kartu 1678872442965: v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to logický a fyzický systém souborů a jaký mají vztah?

### Odpověď (Back)

**Logický** **systém souborů** je tvořen adresářovým stromem. **Fyzický** **systém souborů** je pak organizace dat na disku (DVD, paměti, apod.). Fyzický filesystém připojujeme k logickému pomocí příkazu \(\mathtt{mount}\) na mountpoint (typicky adresář).

## Poznámka Anki 1678872471532

Karty Anki: 1678872471532
GUID: EW;h9]~50o; štítky: bi-adu::p04 bi-ib::02.

Metadata původního zdroje pro kartu 1678872471532: v původním balíčku pozastavená karta.

### Otázka (Front)

Kde lze konfigurovat automatický mount?

### Odpověď (Back)

Automatický mount lze konfigurovat v souboru \(\mathtt{/etc/fstab}\).

## Poznámka Anki 1678873357236

Karty Anki: 1678873357236
GUID: y(5Fxp$e+B; štítky: bi-adu::p04 bi-ib::02 bi-ib::06 bi-spol::18.

### Otázka (Front)

Co je to SWAP? Jak se konfiguruje? Jaký používá konfigurační soubor?

### Odpověď (Back)

SWAP je virtuální adresní prostor, který může přesahovat velikost fyzické paměti. Odkládají se do něj stránky při stránkování. Swapují se zpravidla **anonymní stránky**, což jsou stránky obsahující dynamicky vznikající data. Konfiguruje se pomocí příkazu \(\mathtt{swap}\) a souboru \(\mathtt{/etc/vfstab}\).

