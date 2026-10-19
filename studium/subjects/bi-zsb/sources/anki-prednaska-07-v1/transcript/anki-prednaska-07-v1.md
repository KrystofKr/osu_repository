# BI-ZSB – Přednáška 07

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-zsb/BI-ZSB.apkg; APKG SHA-256 4a7744657502db92b4ca8687b08f3355fbb52a3bc2e87ca5e7c790295dd4a156. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: e234c2761f0a2607fda3b497c3a58fba6f0871307ee12353fc7406deb86bbbeb.
Původní balíčky: BI-ZSB
Rozsah: 9 poznámek, 9 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1700601092107

Karty Anki: 1700601092108
GUID: v2M$nA7vgr; štítky: bi-ib::25 bi-zsb::p07.

### Otázka (Front)

How can an operating system be separated into different security domains?

### Odpověď (Back)

The following means of separating an operating system into multiple security domains exist:

- **write xor execute** (W^X) - a memory page can either be writable or executable but not both,

- **Data Execution Prevention** (DEP),
- **Supervisor Mode Access Prevention** (SMAP) - prevents kernel-level processes from accessing user-level memory,
- **Supervisor Mode Execution Prevention** (SMEP) - prevents kernel-level processes from executing user-level code.

## Poznámka Anki 1700601553740

Karty Anki: 1700601553740
GUID: Ab@T<;{1#:; štítky: bi-ib::25 bi-zsb::p07 ni-pb::21.

### Otázka (Front)

Describe Microsoft Credential Guard.

### Odpověď (Back)

Microsoft Credential Guard is a Microsoft security measure that uses virtualization-based security (VBS) to provide an isolated storage for the Local Security Authority (LSA) to store secrets (such as password hashes or Kerberos ticket-granting tickets).

## Poznámka Anki 1700601800855

Karty Anki: 1700601800855
GUID: sde:m&B:kR; štítky: bi-ib::25 bi-zsb::p07.

### Otázka (Front)

Describe Microsoft Defender Application Guard (MDAG).

### Odpověď (Back)

Microsoft Defender Application Guard (MDAG) is a security measure that uses Hyper-V to open or execute untrusted websites or files in isolated containers.

## Poznámka Anki 1700641552903

Karty Anki: 1700641552903
GUID: FA*cZOa[~E; štítky: bi-zsb::p07.

Metadata původního zdroje pro kartu 1700641552903: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Describe control-flow integrity (CFI).

### Odpověď (Back)

Control-flow integrity (CFI) is a security mechanism that attackers from redirecting the control flow of a program (control-flow hijacking). Multiple implementations of CFI exist; however, the general mechanism of action is that before every indirect jump, the destination address of the jump is verified.

## Poznámka Anki 1700641888045

Karty Anki: 1700641888045
GUID: m.ts!X[]:I; štítky: bi-zsb::p07.

Metadata původního zdroje pro kartu 1700641888045: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Describe secure boot.

### Odpověď (Back)

Secure boot is a security mechanism that uses the Trusted Platform Module (TPM). It ensures that only trusted signed software is loaded during the boot process.

## Poznámka Anki 1700642540916

Karty Anki: 1700642540916
GUID: QKxzv5$cy4; štítky: bi-ib::25 bi-zsb::p07.

### Otázka (Front)

Describe Microsoft Defender System Guard.

### Odpověď (Back)

Microsoft Defender System Guard is a suite of security measures that protect, maintain, and validate system integrity through the boot process and runtime. It encompasses the following mechanisms:

- **Secure Launch** (Dynamic Root of Trust for Measurement) - creates a trusted state of the system from an untrusted state;

- **System Management Mode (SMM)**** protection **- prevents hijacked SMM interrupts from modifying the OS;
- **runtime integrity validation **- self-attestation mechanisms that verify OS integrity, uses the Trusted Platform Module (TPM).

## Poznámka Anki 1700642858468

Karty Anki: 1700642858468
GUID: wvV4;UO;cW; štítky: bi-zsb::p07.

Metadata původního zdroje pro kartu 1700642858468: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Describe Trusted Platform Module (TPM).

### Odpověď (Back)

Trusted Plafrom Module (TPM) is a secure cryptoprocessor standard, which enables the usage of other security measures (such as Secure Boot, disk encryption, key wrapping, and key sealing).

## Poznámka Anki 1700643839381

Karty Anki: 1700643839381
GUID: Q,GdH?#*fI; štítky: bi-ib::25 bi-zsb::p07.

### Otázka (Front)

Describe methods for isolating applications and their pros and cons.

### Odpověď (Back)

The following methods for isolating applications can be used:

| 
      **method** | 
      **description** | 
      **advantages** | 
      **disadvantages** | 

| 
      sandboxing | 
      appliation runs in an environment with restricted access to OS resources | 
      lightweight and fast | 
      limited isolation capabilities | 

| 
      containers | 
      applications share the kernel but are isolated in terms of processes, filesystem, and network | 
      lightweight and fast | 
      limited isolation capabilities
 | 

| 
      virtualization | 
      application runs in a guest OS on top of a host OS | 
      strong isolation | 
      resource intensive |

## Poznámka Anki 1700645402738

Karty Anki: 1700645402738
GUID: Ielb583Q3?; štítky: bi-zsb::p07.

### Otázka (Front)

Describe the threat model of cloud applicatios.

### Odpověď (Back)

Cloud applications adhere to the CIA model:

- **confidentiality** - valuable data and code in a third party infrastructure, resource sharing between co-resident virtual machines;

- **integrity** - data tampering, computation and process integrity;

- **availability** - denial of service (DoS) attacks.

