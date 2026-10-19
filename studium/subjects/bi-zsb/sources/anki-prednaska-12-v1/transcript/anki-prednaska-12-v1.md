# BI-ZSB – Přednáška 12

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-zsb/BI-ZSB.apkg; APKG SHA-256 4a7744657502db92b4ca8687b08f3355fbb52a3bc2e87ca5e7c790295dd4a156. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: e234c2761f0a2607fda3b497c3a58fba6f0871307ee12353fc7406deb86bbbeb.
Původní balíčky: BI-ZSB
Rozsah: 7 poznámek, 7 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1703267322365

Karty Anki: 1703267322365
GUID: F?nD)f$}m[; štítky: bi-zsb::p12.

Metadata původního zdroje pro kartu 1703267322365: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Describe malware and list examples.

### Odpověď (Back)

Malware is a program that is inserted into a system, usually covertly, with the intent of compromising the confidentiality, integrity, or availability of the victim's data, applications, or operating system. Examples of malware include ransomware, spyware nebo adware.

## Poznámka Anki 1703267433635

Karty Anki: 1703267433635
GUID: tX;(8)?!pm; štítky: bi-zsb::p12.

### Otázka (Front)

Describe a blended attack.

### Odpověď (Back)

Blended attack is a type of attack that combines multiple attack methods against one or more vulnerabilities.

## Poznámka Anki 1703268085098

Karty Anki: 1703268085098
GUID: M5B1!e.EbY; štítky: bi-zsb::p12.

### Otázka (Front)

Describe fileless malware.

### Odpověď (Back)

Fileless malware is a type of malware that uses built-in legitimate tools of the operating system to execute malicious actions. It doesn't rely on the creation of files and exists solely in the memory of the computer.

## Poznámka Anki 1703269107119

Karty Anki: 1703269107119
GUID: cDEnwkJ@Z{; štítky: bi-zsb::p12.

### Otázka (Front)

Describe methods for detecting malware on endpoints.

### Odpověď (Back)

The traditional method of detecting malware on endpoints is signature-based. It involves hashing of files and checking their signatures against a database of known malware signatures. In addition, the following modern methods can be used:

- **host-based intrusion prevention system **(HIPS) - monitors for suspicious actions (modification of system files, access to the registy);

- **application control **- allow-lists or block-lists of applications;
- **canary files** - fake files used for the detection of unauthorized data modification (such as by ransomware).

## Poznámka Anki 1703269868926

Karty Anki: 1703269868926
GUID: O;i%25r;{N; štítky: bi-zsb::p12.

### Otázka (Front)

Describe the differences between static and dynamic malware analysis.

### Odpověď (Back)

The key differences between static and dynamic malware analysis are as follows:

| 
      **static malware analysis** | 
      **dynamic malware analysis** | 

| 
      analyzes the code of the malware without executing it
 | 
      analyzes the behavior of the malware as it's being executed | 

| 
      signature-based | 
      behavior-based | 

| 
      doesn't require a sandbox | 
      requires a sandbox | 

| 
      can be hindered by code obfuscation | 
      can defeat code obfuscation |

## Poznámka Anki 1703270374560

Karty Anki: 1703270374560
GUID: w_}agc,`3F; štítky: bi-zsb::p12.

### Otázka (Front)

Describe evasion methods used by malware.

### Odpověď (Back)

Evasion methods used by malware include:

- **anti-disassembly** - special sequences that cause dissasemblers to produce incorrect output,

- **anti-debugging** - checking for active debuggers and avoiding debugging (e.g. by crashing),

- **packing** - compression or encryption of the executable to avoid signature-based detection,
- **anti-virtual machine** - modification of execution when run inside a virtual machine.

## Poznámka Anki 1703270987286

Karty Anki: 1703270987286
GUID: kun2kVQpOw; štítky: bi-zsb::p12.

### Otázka (Front)

When can malware be detected?

### Odpověď (Back)

Malware can be detected:

- **while being downloaded** - the signature of the malware can be recognised from the transmitted packets,

- **after being installed **- detection through periodic scans of the file system or HIPS,
- **later** - detection of communication with a command-and-control server.

