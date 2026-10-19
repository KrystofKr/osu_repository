# BI-ZSB – Přednáška 04

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-zsb/BI-ZSB.apkg; APKG SHA-256 4a7744657502db92b4ca8687b08f3355fbb52a3bc2e87ca5e7c790295dd4a156. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: e234c2761f0a2607fda3b497c3a58fba6f0871307ee12353fc7406deb86bbbeb.
Původní balíčky: BI-ZSB
Rozsah: 12 poznámek, 12 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1697614606108

Karty Anki: 1697614606108
GUID: J0K8)b9o#.; štítky: bi-ib::23 bi-zsb::p04 ni-pb::20.

### Otázka (Front)

What is a checksum?

### Odpověď (Back)

Checksum is a value that is dependent on the content of the source data object. Checksums are used to verify data integrity and to detect errors that might have been introduced by data storage and transmission.

## Poznámka Anki 1697614930295

Karty Anki: 1697614930295
GUID: HjvjetJovS; štítky: bi-ib::23 bi-zsb::p04 ni-pb::20.

### Otázka (Front)

What is a disk image?

### Odpověď (Back)

A disk image is a file or a set of files that captures a snapshot of the content and structure of a memory device. Traditionally, disk images were taken as bit-by-bit copies; however, compression and deduplication is commonly used to reduce the size of the file set.

## Poznámka Anki 1697617003009

Karty Anki: 1697617003010
GUID: bj4{5iHOD7; štítky: bi-ib::23 bi-zsb::p04 ni-pb::20.

### Otázka (Front)

What is a chain of custody?

### Odpověď (Back)

Chain of custody is a process that tracks the movement and handling of evidence by documenting each person who came in contact with the evidence, time or date it was collected or transferred, and the purpose for the transfer.

## Poznámka Anki 1697617627446

Karty Anki: 1697617627446
GUID: m`ioj[m&$a; štítky: bi-ib::23 bi-zsb::p04 ni-pb::20.

### Otázka (Front)

What is a hardware write-blocker?

### Odpověď (Back)

Hardware write-blocker sometimes called forensic disk controller is a disk controller that is used for the purpose of gaining read-only access to a memory device without the risk of influencing its contents.

## Poznámka Anki 1698218443253

Karty Anki: 1698218443254
GUID: CxoKL>:0Fl; štítky: bi-ib::23 bi-zsb::p04 ni-pb::20.

### Otázka (Front)

What forensic disk image formats exist?

### Odpověď (Back)

Forensic disk images can be stored using the following formats:

- Advanced Forensic File Format (AFF4),

- generic forensic zip (GFZIP),

- Expert Witness Format (EWF),

- EnCase Image File Format (E01 and EX01).

## Poznámka Anki 1698234900345

Karty Anki: 1698234900345
GUID: nCm8VTQ>1A; štítky: bi-ib::23 bi-zsb::p04 ni-pb::20.

### Otázka (Front)

What are the conditions of evidence validity (acceptability)?

### Odpověď (Back)

The two conditions of evicendce validity (acceptability) are:

- chain of custody,

- evidence integrity.

## Poznámka Anki 1698235406086

Karty Anki: 1698235406086
GUID: m>FliMN8kZ; štítky: bi-zsb::p04.

Metadata původního zdroje pro kartu 1698235406086: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

What are the stages of forensic analysis?

### Odpověď (Back)

Forensic analysis usually consists of the following stages:

- **identification** - finding evidence,

- **preservation** - isolating data and ensuring preservation of its initial state,

- **analysis** - reconstructing data and drawing conclusions,

- **documentation** - documenting the process for future reproduction and non-repudiation,

- **presentation** - presenting the results to a non-professional audience.

## Poznámka Anki 1701886034763

Karty Anki: 1701886034763
GUID: F1mzR}tg}r; štítky: bi-ib::23 bi-zsb::p04 ni-pb::20.

### Otázka (Front)

Describe the diferences between a raw disk image and a forensic disk image format.

### Odpověď (Back)

A raw disk image represents the data as-is and has the advantage of portability. In constrast, forensic disk images usually contain metadata, have built-in integrity verification (such as checksums), and often leverage compression.

## Poznámka Anki 1718218692798

Karty Anki: 1718218692798
GUID: GOPiKrgbTu; štítky: bi-ib::23 bi-zsb::p04 ni-pb::20.

### Otázka (Front)

Describe data acquisition in the context of digital forensics.

### Odpověď (Back)

Data acquisition is the process of gathering all data related to a digital forensic investigation. This process often uses:

- write blockers,

- forensic file formats or raw bit-by-bit copies,
- hashing and checksums.

## Poznámka Anki 1718219782461

Karty Anki: 1718219782461
GUID: ezh#s~*vNB; štítky: bi-ib::23 bi-zsb::p04 ni-pb::20.

### Otázka (Front)

Describe the Expert Witness Format (EWF).

### Odpověď (Back)

Expert Witness Format (EWF) is a type of forensic disk image format. EWF images consist of multiple files (segments) each with their own header that contains metadata and a checksum (Adler-32). Each file is made up of multiple 32 kb chunks that are compressed. This allows access to any offset within the image without the need for full decompression. EWF served as the basis for the EnCase Image File Format (E01).

## Poznámka Anki 1718220068697

Karty Anki: 1718220068697
GUID: nMs:wia/Yw; štítky: bi-ib::23 bi-zsb::p04 ni-pb::20.

### Otázka (Front)

Describe the EnCase Image File Format (E01).

### Odpověď (Back)

EnCase Image File Format (E01) is one of the most used forensic disk image formats which is based on the Expert Witness Format (EWF). In addition to the perks of EWF, E01 supports:

- larger segments,
- more effective compression (bzip2),
- encryption (AES-256),
- multithreaded access to data.

## Poznámka Anki 1718220294606

Karty Anki: 1718220294606
GUID: vcM&MxFN3|; štítky: bi-ib::23 bi-zsb::p04.

### Otázka (Front)

List common tools used in forensic analysis.

### Odpověď (Back)

Forensic analysis uses the following tools:

- write blocker,

- forensic disc duplicator,

- storage media interfaces (SATA, miniSATA, PCIe),
- software for data acquisition,
- software for data analysis,
- software for the analysis of mobile devices.

