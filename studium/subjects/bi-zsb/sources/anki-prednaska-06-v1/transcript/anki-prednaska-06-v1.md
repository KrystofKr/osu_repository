# BI-ZSB – Přednáška 06

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-zsb/BI-ZSB.apkg; APKG SHA-256 4a7744657502db92b4ca8687b08f3355fbb52a3bc2e87ca5e7c790295dd4a156. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: e234c2761f0a2607fda3b497c3a58fba6f0871307ee12353fc7406deb86bbbeb.
Původní balíčky: BI-ZSB
Rozsah: 5 poznámek, 5 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1700594970642

Karty Anki: 1700594970642
GUID: g{eR,,$PQc; štítky: bi-zsb::p06.

### Otázka (Front)

Describe a bring your own vulnerable driver (BYOVD) attack.

### Odpověď (Back)

Bring your own vulnerable driver (BYOVD) attack is an attack in which an attacker brings a legitimately signed vulnerable driver to execute malicious actions with kernel-level privileges on a target system.

## Poznámka Anki 1700595451461

Karty Anki: 1700595451462
GUID: BNK@Xp3SSS; štítky: bi-zsb::p06.

### Otázka (Front)

Describe a bootkit.

### Odpověď (Back)

Bootkit is a type of malware which usually targets the Master Boot Record (MBR). By attaching itself to the MBR, the bootkit is able to execute prior to the operating system and bypass detection mechanisms.

## Poznámka Anki 1700595773544

Karty Anki: 1700595773544
GUID: g=u/k,Yy4Y; štítky: bi-zsb::p06.

### Otázka (Front)

Describe the row hammer attack.

### Odpověď (Back)

Row hammer attack is an attack targeted at DRAM. Since DRAM cells are packed densely together, repeatedly accesing a specific memory row may cause it to leak an electrical charge and modify the contents of another memory row. The row hammer attack can be used to alter page table entries and escalate privileges.

## Poznámka Anki 1700596324805

Karty Anki: 1700596324805
GUID: c]p^2|4fvr; štítky: bi-zsb::p06.

### Otázka (Front)

Describe the double-fetch vulnerability.

### Odpověď (Back)

Double-fetch vulnerability is a type of time-of-check to time-of-use (TOCTOU) vulnerability which occurs when a privileged process fetches data twice, first for security checks, and then later for actual processing. In this situation a malicious process may modify the data in the time frame between the security check and processing.

## Poznámka Anki 1700597400728

Karty Anki: 1700597400728
GUID: lw;srsXcd]; štítky: bi-ib::25 bi-zsb::p06.

### Otázka (Front)

Describe operating system design models.

### Odpověď (Back)

Operating systems are mostly designed in accordance with one of the following models:

- **single domain** - no isolation, applications and the OS are in the same security domain;

- **monolithic OS** - applications and the OS are separated into different security domains;

- **microkernel-based multi-server OS** - components of the OS are separated into different security domains;

- **unikernel (library OS)** - applications are statically linked with minimal OS code and run on top of a lightweight hypervisor-like kernel.

