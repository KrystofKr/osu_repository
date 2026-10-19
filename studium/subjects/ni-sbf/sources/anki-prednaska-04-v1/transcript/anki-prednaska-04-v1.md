# NI-SBF – Přednáška 04

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/ni-sbf/NI-SBF.apkg; APKG SHA-256 eea8ecb13bdb56a02027b1cf6860588c0d4e44a6ec0b1d9b60c8cf7bc0df0806. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: e39cc77808ce484ac431215d36a50c128a0bf18ed66d8b544ffa1d5eb2a9d7be.
Původní balíčky: NI-SBF
Rozsah: 4 poznámek, 4 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1729082538178

Karty Anki: 1729082538178
GUID: bx!/xaFCS2; štítky: ni-pb::20 ni-sbf::p04.

### Otázka (Front)

Describe memory forensics.

### Odpověď (Back)

Memory forensics is a branch of digital forensics that analyzes volatile data in a computer's memory. This is particularly important to capture encryption keys or to detect subjects that don't leave a trace on the disk of the computer, such as file-less malware. Memory forensic analysis usually consists of the following phases:

- **acquire** - acquire data (hibernation files, swap files);

- **context** - establish context,

- **analyze** - analyze data for significant elements.

## Poznámka Anki 1729083394953

Karty Anki: 1729083394953
GUID: zaZ(y;9UnX; štítky: ni-pb::20 ni-sbf::p04.

### Otázka (Front)

Describe the sources for data acquisition in memory forensics.

### Odpověď (Back)

Sources for data acquisition in memory forensics depend on the circumstances of the analyzed system:

- **virtual machines** - virtual disks, snapshots, clones;

- **stopped systems** - hibernation files, page files, swap files;
- **running systems without root access **- hardware methods;

- **running systems with root access** - software methods.

## Poznámka Anki 1729084483616

Karty Anki: 1729084483616
GUID: jK]97,}K[>; štítky: ni-pb::20 ni-sbf::p04.

### Otázka (Front)

Describe the approaches to data acquisition in memory forensics.

### Odpověď (Back)

Data acquisition in memory forensics can be done using the following approaches:

- **local acquisition to removable media** - risk of contamination through the removable media,

- **remote acquisition over the network** - risk of exposure of cofidential data during the transfer.

## Poznámka Anki 1729085426909

Karty Anki: 1729085426909
GUID: L6Fd@#fhj(; štítky: ni-sbf::p04.

### Otázka (Front)

Describe types of code injection.

### Odpověď (Back)

The following types of code injection exist:

- **remote DLL injection** - malicious process forces the target process to load and execute a DLL from disk,

- **remote code injection** - malicious process writes code into the memory of the target process and forces it to execute it,

- **reflective DLL injection** - malicious process writes a DLL into the memory of the target process and forces it to execute it,

- **hollow process injection** - malicious process starts a new instance of a legitimate process and replaces its code with malicious code.

