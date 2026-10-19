# NI-SBF – Přednáška 05

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/ni-sbf/NI-SBF.apkg; APKG SHA-256 eea8ecb13bdb56a02027b1cf6860588c0d4e44a6ec0b1d9b60c8cf7bc0df0806. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: e39cc77808ce484ac431215d36a50c128a0bf18ed66d8b544ffa1d5eb2a9d7be.
Původní balíčky: NI-SBF
Rozsah: 12 poznámek, 12 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1729687794555

Karty Anki: 1729687794555
GUID: NnTe>{;Tva; štítky: ni-sbf::p05.

### Otázka (Front)

Describe data storage layers.

### Odpověď (Back)

Data storage usually consists of the following layers:

- **physical layer** - memory medium;
- **file system layer **- partition information;

- **data layer** - clusters and sectors;

- **metadata layer** - structural information for the filesystem;

- **file name layer** - directory hierarchy, file naming.

## Poznámka Anki 1729687835575

Karty Anki: 1729687835575
GUID: zJd$th3y]p; štítky: ni-sbf::p05.

Metadata původního zdroje pro kartu 1729687835575: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

What are computer files and metadata?

### Odpověď (Back)

Computer file is a logically grouped set of data of a defined format stored on a data medium and referenced by a unique name. Additionally, computer files are often asociated with metadata which carry information such as their size, owners, or access permissions.

## Poznámka Anki 1729687851330

Karty Anki: 1729687851330
GUID: J{*z}X^1*y; štítky: ni-sbf::p05.

Metadata původního zdroje pro kartu 1729687851330: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

What is file carving?

### Odpověď (Back)

File carving is the process of recovering files in the absence of their metadata. This is generally done by searching the file system for magic numbers (file headers). The drawback of this method is that it is not usually possible to restore the metadata along with the files.

## Poznámka Anki 1729687864250

Karty Anki: 1729687864250
GUID: c)s$?l9deZ; štítky: ni-sbf::p05.

Metadata původního zdroje pro kartu 1729687864250: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

What is slack space?

### Odpověď (Back)

Slack space refers to unused space in a file cluster (allocation unit). This space may hold residual data of a deleted file that was allocated in this cluster before being overwritten.

 [Obrázek: paste-ac40ed3ec323b1c4b6dbeabf3cfd21a6e58f9a42.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1729687877889

Karty Anki: 1729687877889
GUID: dQ9z$0|)rA; štítky: ni-sbf::p05.

Metadata původního zdroje pro kartu 1729687877889: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Describe a file system (FS). List examples.

### Odpověď (Back)

File system (FS) is a system used for file organization and access. It usually consists of the following layers:

- **logical** - file access, operations and security, consists of a directory tree;

- **virtual** - abstraction layer, provides a unified interface for various file system implementations;

- **physical** - data access and modification, organizes data on a memory medium.

Data within a file system is usually split into the following units:

- **sector** - smallest addressable unit (defined by the memory medium)

- **cluster** - smallest allocatable unit consisting of multiple sectors (defined by the file system),

Examples of file systems include FAT, ext, UFS, or NTFS.

## Poznámka Anki 1729687895212

Karty Anki: 1729687895212
GUID: zDgyBer]T?; štítky: ni-sbf::p05.

Metadata původního zdroje pro kartu 1729687895212: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Describe file system forensic analysis.

### Odpověď (Back)

File system forensic analysis refers to the process of retrieving unstructured, deleted, or hidden data in a file system that are relevant to a digital forensic investigation. This is generally possible because deleting a file within a file system merely marks its clusters as free instead of securely removing its data. File system forensic analysis is usually based on:

- data carving,
- metadata,
- artifacts,

- slack space.

## Poznámka Anki 1729688024530

Karty Anki: 1729688024530
GUID: e,8Zdb.OoX; štítky: ni-pb::20 ni-sbf::p05.

### Otázka (Front)

Describe data stream carving.

### Odpověď (Back)

Data stream carving is a type of file carving that searches for fragments of files instead of complete files.

## Poznámka Anki 1729689317332

Karty Anki: 1729689317332
GUID: vF)$?zr<9R; štítky: ni-pb::20 ni-sbf::p05.

### Otázka (Front)

Describe approaches for the validation of carved objects.

### Odpověď (Back)

Carved objects can be validated using the followed approaches:

- validation of headers and footers,
- validation of known structures,
- semantic validation.

## Poznámka Anki 1729689405455

Karty Anki: 1729689405455
GUID: OZ,F;B-j->; štítky: ni-sbf::p05.

Metadata původního zdroje pro kartu 1729689405455: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Describe the New Technology File System (NTFS).

### Odpověď (Back)

New Technology File System (NTFS) is a journalling file system which is mainly used in Windows. It supports compression, access control, and encryption. One of the crucial components of NTFS is the Master File Table (MFT) which stores metadata of all directories and files. In case of corruption, NTFS stores an additional partial copy of the MFT called the MFT mirror.

## Poznámka Anki 1729690535574

Karty Anki: 1729690535574
GUID: M1IxK{:3)/; štítky: ni-pb::20 ni-sbf::p05.

### Otázka (Front)

Describe resident and non-resident files in the New Technology File System (NTFS).

### Odpověď (Back)

Resident New Technology File System (NTFS) files are files that are small enough to be stored in the Master File Table (MFT) along with their metadata. Files other than resident are called non-resident files.

## Poznámka Anki 1729690679175

Karty Anki: 1729690679175
GUID: j9T_Vt[{e9; štítky: ni-pb::20 ni-sbf::p05.

### Otázka (Front)

Describe internal files of the New Technology File System (NTFS).

### Odpověď (Back)

Internal files of the New Technology File System (NTFS) are files that store administrative data. Examples of NTFS internal files include:

- \(\texttt{\$MFT}\) - Master File Table (MFT),

- \(\texttt{\$LogFile}\) - transactional log of changes made to the MFT, used for journaling;

- \(\texttt{\$UsnJrnl}\) - log of changes made to files and directories.

## Poznámka Anki 1729692667342

Karty Anki: 1729692667343
GUID: y*)PEaM2|v; štítky: ni-pb::20 ni-sbf::p05.

### Otázka (Front)

Describe timestomping.

### Odpověď (Back)

Timestomping is a technique used in digital forensics, whereby attackers modify the timestamps of files and directories to hide their actions or impede forensic investigation.

