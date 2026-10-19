# BI-ZSB – Přednáška 05

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-zsb/BI-ZSB.apkg; APKG SHA-256 4a7744657502db92b4ca8687b08f3355fbb52a3bc2e87ca5e7c790295dd4a156. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: e234c2761f0a2607fda3b497c3a58fba6f0871307ee12353fc7406deb86bbbeb.
Původní balíčky: BI-ZSB
Rozsah: 9 poznámek, 9 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1698219446065

Karty Anki: 1698219446066
GUID: k4BDVGWCrK; štítky: bi-ib::24 bi-zsb::p05 ni-pb::20.

### Otázka (Front)

What are computer files and metadata?

### Odpověď (Back)

Computer file is a logically grouped set of data of a defined format stored on a data medium and referenced by a unique name. Additionally, computer files are often asociated with metadata which carry information such as their size, owners, or access permissions.

## Poznámka Anki 1698220282173

Karty Anki: 1698220282174
GUID: ki&C~Gl_LG; štítky: bi-ib::24 bi-zsb::p05.

### Otázka (Front)

What are the approaches for computer file format recognition?

### Odpověď (Back)

Computer file formats can be recognized using:

- **suffix **(extension) - last part of the filename, lower reliability;

- **magic number** (file header) - unique sequence inside the file itself (type of metadata), higher reliability.

## Poznámka Anki 1698222448233

Karty Anki: 1698222448233
GUID: x]j2T#uL3K; štítky: bi-zsb::p05.

Metadata původního zdroje pro kartu 1698222448233: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

What is file carving?

### Odpověď (Back)

File carving is the process of recovering files in the absence of their metadata. This is generally done by searching the file system for magic numbers (file headers). The drawback of this method is that it is not usually possible to restore the metadata along with the files.

## Poznámka Anki 1698222465399

Karty Anki: 1698222465399
GUID: qxo??`(z#?; štítky: bi-zsb::p05.

Metadata původního zdroje pro kartu 1698222465399: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

What is slack space?

### Odpověď (Back)

Slack space refers to unused space in a file cluster (allocation unit). This space may hold residual data of a deleted file that was allocated in this cluster before being overwritten.

 [Obrázek: paste-ac40ed3ec323b1c4b6dbeabf3cfd21a6e58f9a42.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1718284747718

Karty Anki: 1718284747718
GUID: l>B3>Y^Fm?; štítky: bi-ib::24 bi-zsb::p05 ni-pb::20.

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

## Poznámka Anki 1718285483032

Karty Anki: 1718285483032
GUID: rc%>H,eWx@; štítky: bi-ib::24 bi-zsb::p05 ni-pb::20.

### Otázka (Front)

Describe file system forensic analysis.

### Odpověď (Back)

File system forensic analysis refers to the process of retrieving unstructured, deleted, or hidden data in a file system that are relevant to a digital forensic investigation. This is generally possible because deleting a file within a file system merely marks its clusters as free instead of securely removing its data. File system forensic analysis is usually based on:

- data carving,
- metadata,
- artifacts,

- slack space.

## Poznámka Anki 1718286950726

Karty Anki: 1718286950726
GUID: yh1/QAb%G}; štítky: bi-ib::24 bi-zsb::p05 ni-pb::20.

### Otázka (Front)

Describe the New Technology File System (NTFS).

### Odpověď (Back)

New Technology File System (NTFS) is a journalling file system which is mainly used in Windows. It supports compression, access control, and encryption. One of the crucial components of NTFS is the Master File Table (MFT) which stores metadata of all directories and files. In case of corruption, NTFS stores an additional partial copy of the MFT called the MFT mirror.

## Poznámka Anki 1718287253904

Karty Anki: 1718287253905
GUID: HcyM~z,Zw; štítky: bi-ib::24 bi-zsb::p05 ni-pb::20.

### Otázka (Front)

Describe the extended file system (ext).

### Odpověď (Back)

Extended file system (ext) is a family of file systems mainly used in Linux with the latest version being ext4. Ext4 is a journaling file system which supports pre-allocation, encryption, and the use of checksums for its log. The metadata of all directories and files is stored in the i-node table.

## Poznámka Anki 1718288742438

Karty Anki: 1718288742438
GUID: k`KbSS3QT]; štítky: bi-ib::24 bi-zsb::p05 ni-pb::20.

### Otázka (Front)

Compare the approaches to the recovery of deleted data during a file system forensic analysis.

### Odpověď (Back)

During a file system forensic analysis deleted data can be recovered either using metadata and file system tables (FAT, MFT, i-node table) or by searching the file system for magic numbers (file carving). Using these approaches we recieve:

| 
      file system tables | 
      magic numbers (file carving) | 

| 
      directory structure | 
      raw data blocks | 

| 
      file and directory names | 
      no file and directory names | 

| 
      file and directory metadata | 
      no file and directory metadata | 

| 
       | 
      possibly a large amount of unrelated data |

