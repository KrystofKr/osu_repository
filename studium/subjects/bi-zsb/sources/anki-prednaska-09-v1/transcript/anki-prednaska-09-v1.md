# BI-ZSB – Přednáška 09

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-zsb/BI-ZSB.apkg; APKG SHA-256 4a7744657502db92b4ca8687b08f3355fbb52a3bc2e87ca5e7c790295dd4a156. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: e234c2761f0a2607fda3b497c3a58fba6f0871307ee12353fc7406deb86bbbeb.
Původní balíčky: BI-ZSB
Rozsah: 13 poznámek, 13 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1700763571678

Karty Anki: 1700763571678
GUID: I+1T+@K&o1; štítky: bi-ib::25 bi-zsb::p09.

### Otázka (Front)

Describe primitives for isolation and mediation used in operating systems.

### Odpověď (Back)

The following basic primitives can be used for isolation and mediation in operating systems:

- authentication,
- authorization,
- accounting and auditing.

In addition, more advanced approaches can be used, such as:

- access control lists,

- capabilities,

- process isolation.

## Poznámka Anki 1700764116861

Karty Anki: 1700764116861
GUID: oNUkq|.*kF; štítky: bi-ib::25 bi-zsb::p09.

### Otázka (Front)

Describe process isolation. Give examples of process isolation implementations.

### Odpověď (Back)

Process isolation is achieved by restricting the process to a set of resources (confinement), which is implemented using bounds. Bounds ensure the compliance of the process with the restrictions and define the resources the process can access. Examples of process isolation implementations include the Android Application Sandbox and iOS App Sandbox.

## Poznámka Anki 1700764776810

Karty Anki: 1700764776810
GUID: yGbra._G[q; štítky: bi-ib::25 bi-zsb::p09.

### Otázka (Front)

Describe trusted computing base (TCB).

### Odpověď (Back)

Trusted computing base (TCB) includes all hardware, firmware, and software components of the system that are critical to its security. The TCB contains, among others, the reference monitor.

## Poznámka Anki 1700765802870

Karty Anki: 1700765802870
GUID: eb*U4is`N%; štítky: bi-ib::25 bi-zsb::p09.

### Otázka (Front)

Describe the reference monitor.

### Odpověď (Back)

Reference monitor is a set of design requirements on a reference validation mechanism that enforces an access control policy over all subjets and objects within a system. It should meet the following requirements:

- **always invoked **(complete mediation) - every access to every object must be authorized by the reference monitor,

- **tamperproof** - reference monitor should be isolated from the rest of the system,

- **verifiable** - amenable to tests and evaluation.

## Poznámka Anki 1700766212711

Karty Anki: 1700766212712
GUID: kc$|N+_h|-; štítky: bi-zsb::p09.

Metadata původního zdroje pro kartu 1700766212712: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Describe multi-level security (MLS).

### Odpověď (Back)

Multi-level security (MLS) is an information processing concept which defines classifications and categories of data with different security levels. The access to the data is then only permitted to users with the appropriate security clearance.

## Poznámka Anki 1700766741893

Karty Anki: 1700766741893
GUID: AYYogKb/+9; štítky: bi-ib::25 bi-zsb::p09.

### Otázka (Front)

Describe multi-category security (MCS).

### Odpověď (Back)

Multi-category security (MCS) is an enhancement of the multi-level security (MLS) concept. MCS allows the definition of categories and their assigment to subjects and objects. Subjects are then allowed to only access objects in the same categories as their own.

## Poznámka Anki 1700767041239

Karty Anki: 1700767041239
GUID: hq*!7c!EQb; štítky: bi-ib::01 bi-ib::25 bi-zsb::p09.

### Otázka (Front)

What is the difference between discretionary access control (DAC) and mandatory access control (MAC)?

### Odpověď (Back)

Both discretionary access control (DAC) and mandatory access control (MAC) refer to the means of restricting access to objects based on the identity of subjects or their group memberships. DAC allows a subject in control of an object to pass that permission onto another subject, whereas MAC is only configurable by a highly privileged subject, such as a system administrator.

## Poznámka Anki 1700767399257

Karty Anki: 1700767399257
GUID: Q<MJ@kA?b^; štítky: bi-zsb::p09.

Metadata původního zdroje pro kartu 1700767399257: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Describe a Windows discretionary access control list (DACL).

### Odpověď (Back)

Windows discretionary access control list (DACL) is a list of access control entries (ACE) that identifies trustees that are allowed or denied access to a securable object.

## Poznámka Anki 1700767644790

Karty Anki: 1700767644790
GUID: NfU=/(Eznk; štítky: bi-zsb::p09.

Metadata původního zdroje pro kartu 1700767644790: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Describe a Windows system access control list (SACL).

### Odpověď (Back)

Windows system access control list (SACL) is a list of access control entries (ACE) that specify the types of access by a specified trustee to a securable object that will be loged in the security event log.

## Poznámka Anki 1700769254832

Karty Anki: 1700769254832
GUID: QQ)?7_Wc[#; štítky: bi-ib::01 bi-ib::25 bi-zsb::p09.

### Otázka (Front)

Describe SELinux.

### Odpověď (Back)

SELinux is a Linux security kernel module that provides support for mandatory access control (MAC) and other security measures. It consists of these core components:

- **subject** - requests access to an object,
- **object manager **- manages access to an object and enforces restrictions,

- **security server **- makes decisions regarding subjects' rights when accessing objects based on the security policy,

- **security policy** - describes access rules,

- **access vector cache** - improves performance by caching the decisions of the security server.

## Poznámka Anki 1700769880808

Karty Anki: 1700769880808
GUID: )X9${ISE,; štítky: bi-ib::01 bi-ib::25 bi-zsb::p09.

### Otázka (Front)

Describe SELinux security context.

### Odpověď (Back)

SELinux associates every subject and object with a security context which is later used by the security server to decide whether access is allowed or denied based on the security policy. The security context has the following format:
\[\mathtt{user} \text : \mathtt{role} \text : \mathtt{type[}\text : \mathtt{range]},\]where

- \(\mathtt{user}\) is a SELinux user,

- \(\mathtt{role}\) is a SELinux role,

- \(\mathtt{type}\) either defines which processes a subject can access when associated with a process, or the permissions a subject has to an object when associated with an object,

- \(\mathtt{range}\) specifies security levels and categories as defined by multi-level security (MLS) and multi-category security (MCS).

## Poznámka Anki 1700770132729

Karty Anki: 1700770132729
GUID: w!~.v$+fSU; štítky: bi-ib::01 bi-ib::25 bi-zsb::p09.

### Otázka (Front)

Describe AppArmor.

### Odpověď (Back)

AppArmor is a Linux security kernel module that provides support for mandatory access control (MAC) and other security measures. In contrast to SELinux, AppArmor works with paths rather than security contexts and therefore does not rely on filesystem support.

## Poznámka Anki 1700770430884

Karty Anki: 1700770430884
GUID: J7yc)*7W]7; štítky: bi-ib::25 bi-zsb::p09.

### Otázka (Front)

Describe Windows Mandatory Integrity Control (MIC).

### Odpověď (Back)

Windows Mandatory Integrity Control (MIC) is a security feature that supplements mandatory access control (MAC) by assigning an integrity level to every securable object and every security princial. Integrity levels determine the levels of access or protection so that a security principal with a low integrity level cannot access a securable object with a higher integrity level.

