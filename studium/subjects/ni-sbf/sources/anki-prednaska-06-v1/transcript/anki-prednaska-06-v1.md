# NI-SBF – Přednáška 06

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/ni-sbf/NI-SBF.apkg; APKG SHA-256 eea8ecb13bdb56a02027b1cf6860588c0d4e44a6ec0b1d9b60c8cf7bc0df0806. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: e39cc77808ce484ac431215d36a50c128a0bf18ed66d8b544ffa1d5eb2a9d7be.
Původní balíčky: NI-SBF
Rozsah: 8 poznámek, 8 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1730295299144

Karty Anki: 1730295299144
GUID: A$;AflU31|; štítky: ni-sbf::p06.

Metadata původního zdroje pro kartu 1730295299144: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

What are forensic artifacts? List examples.

### Odpověď (Back)

Forensic artifacts are data that are generated or left behind by activities of a user on a digital device. This includes logs, browsing history, swap, or hibernation files.

## Poznámka Anki 1730295906921

Karty Anki: 1730295906921
GUID: GURcauLaXz; štítky: ni-pb::20 ni-sbf::p06.

### Otázka (Front)

Describe the sources for forensic analysis of a compromised Windows endpoint.

### Odpověď (Back)

Forensic analysis of a compromised Windows endpoint can use the following sources:

- **browser usage** - cookies, history;
- **program execution** - event log, prefetch files;
- **file deletion or file knowledge** - thumbcache, recycle bin;
- **file access or file creation** - shortcuts, jump lists;
- **file download** - email attachments, browser usage;
- **account usage** - event log.

## Poznámka Anki 1730296152028

Karty Anki: 1730296152028
GUID: yGN$S!/Pg0; štítky: ni-pb::20 ni-sbf::p06.

### Otázka (Front)

Describe the Windows registry.

### Odpověď (Back)

Windows registry is a central hierarchical database used to store information necessary to configure the system for users, applications, and hardware devices. It is stored as a binary data structure and consists of several top-level keys, such as \(\texttt{HKEY_CURRENT_USER}\) or \(\texttt{HKEY_LOCAL_MACHINE}\).

## Poznámka Anki 1730296556155

Karty Anki: 1730296556155
GUID: B;8Q^tUckL; štítky: ni-pb::20 ni-sbf::p06.

### Otázka (Front)

Describe the Windows event log.

### Odpověď (Back)

Windows event log stores information about events that occur in the system. These events are categorized as follows:

- **system** - events related to system components, hardware, drivers;

- **application **- events related to installed applications;

- **setup **- events related to installers;
- **security** - events related to security, such as access control events.

## Poznámka Anki 1730297663882

Karty Anki: 1730297663883
GUID: pSfYZ*Y*WD; štítky: ni-pb::20 ni-sbf::p06.

### Otázka (Front)

Describe Windows prefetch files.

### Odpověď (Back)

Windows prefetch files are files used to speed up the loading of applications. They can also be used as forensic artifacts that track the execution of programs as they contain the following information:

- name of the executable,
- timestamp of the last execution,
- run count.

## Poznámka Anki 1730300330396

Karty Anki: 1730300330396
GUID: uv),{s/ap3; štítky: ni-pb::20 ni-sbf::p06.

### Otázka (Front)

Describe Windows thumbcache.

### Odpověď (Back)

Windows thumbcache stores thumbnails of file types such as JPEG, PNG, or PDF. It can be used as a forensic artifact because files' thumbnails will remain cached even after their deletion.

## Poznámka Anki 1730300617159

Karty Anki: 1730300617159
GUID: ANF1M!A_Hj; štítky: ni-pb::20 ni-sbf::p06.

### Otázka (Front)

Describe Windows recycle bin.

### Odpověď (Back)

Windows recycle bin is a temporary storage for deleted items and may be used as a source of forensic artifacts. Each deleted item is split into the two following files:

- \(\texttt{\$I<random-string>}\) - file containing the metadata of the deleted item,

- \(\texttt{\$R<random-string>}\) - file containing the actual data of the deleted item.

## Poznámka Anki 1730300891215

Karty Anki: 1730300891216
GUID: lm1|&q;/S4; štítky: ni-pb::20 ni-sbf::p06.

### Otázka (Front)

Describe Windows jump lists.

### Odpověď (Back)

Windows jump lists provide quick access to recently used application files and common tasks. They can be used as a forensic artifact as they provide information about users' activities, such as file access, modification, or creation.

