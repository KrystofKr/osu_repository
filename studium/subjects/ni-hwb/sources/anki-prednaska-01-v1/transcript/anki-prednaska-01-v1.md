# NI-HWB – Přednáška 01

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/ni-hwb/NI-HWB.apkg; APKG SHA-256 a65d26859a40bf4bc1c7dc8804425425d385ad2331d944e375f0fd10ce6e3550. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: ac319344d2de2cb4060d944b0c9d196f41ac858e59c961026ffe267a795b1399.
Původní balíčky: NI-HWB
Rozsah: 15 poznámek, 15 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1739786957881

Karty Anki: 1739786957881
GUID: vKP_*s<amT; štítky: ni-hwb::p01.

Metadata původního zdroje pro kartu 1739786957881: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Describe a smart cart. Which authentication factor does it represent?

### Odpověď (Back)

Smart card is typically a plastic card which contains an integrated circuit. It represents the ownership authentication factor.

## Poznámka Anki 1739787045181

Karty Anki: 1739787045182
GUID: DA[^Ju8tKd; štítky: ni-hwb::p01.

Metadata původního zdroje pro kartu 1739787045182: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Describe the types of smart card interfaces.

### Odpověď (Back)

Smart card interfaces can be categorized as follows:

- **contact** (USB);
- **contactless** (RFID, NFC).

Aditionally, if the smart card contains both contact and contactless interfaces, we discern the following interfaces:

- **hybrid** - each interface uses its own chip,

- **dual **- both interfaces use the same chip.

## Poznámka Anki 1739787069926

Karty Anki: 1739787069926
GUID: O3,%%@HR)*; štítky: ni-hwb::p01.

Metadata původního zdroje pro kartu 1739787069926: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Describe ISO 14443.

### Odpověď (Back)

ISO 14443 is a standard that defines the contactless interface of smart cards with cryptographic functions. The interface uses proximity coupling and the frequency of 13.56 MHz.

## Poznámka Anki 1739787116344

Karty Anki: 1739787116345
GUID: De4x#BN^oe; štítky: ni-hwb::p01.

Metadata původního zdroje pro kartu 1739787116345: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Describe the internal structure of a smart card.

### Odpověď (Back)

Basic smart cards merely contain connected contancs, resonant circuits, or similar. More advanced smart cards use memory either in the form of ROM, EEPROM or secure memory (such as MIFARE Classic). Modern smart cards contain programmable and configurable computers (e.g. Java Cards). The internal structure of such computer is as follows:

- **processing units** - CPU, cryptographic coprocessor;
- **memory** - RAM, ROM, EEPROM;

- **interface**;

- **sensors**.

## Poznámka Anki 1739788194227

Karty Anki: 1739788194227
GUID: CnQ:*~%5Y{; štítky: ni-hwb::p01.

Metadata původního zdroje pro kartu 1739788194227: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Describe the cryptographic schemes used in smart cards.

### Odpověď (Back)

Smart cards may use the following cryptohraphic schemes:

- **symmetric cryptography** - a secret key is shared between the card and the terminal,

- **asymmetric cryptography** - the card has its own private and public key.

## Poznámka Anki 1739788222233

Karty Anki: 1739788222234
GUID: F*<6U6!:AJ; štítky: ni-hwb::p01.

Metadata původního zdroje pro kartu 1739788222234: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Describe the application protocol data unit (APDU) according to ISO 7816.

### Odpověď (Back)

Application protocol data unit (APDU) is a communication unit used between smart cards and terminals. It has the following structure:

 [Obrázek: paste-ae65b14bea9d5f93000cdaae3eacde1819e077f1.jpg; soubor je v media/ v doprovodném ZIP] 

The fields represent the following:

- \(\mathtt{CLA}\) - instruction class,

- \(\mathtt{INS}\) - instruction code,

- \(\mathtt{P1}\) a \(\mathtt{P2}\) - parameters,

- \(\mathtt{L_c}\) - length of the \(\mathtt{Data}\) field,

- \(\mathtt{Data}\) - instruction or response data,

- \(\mathtt{L_e}\)- expected response length.

- \(\mathtt{SW1}\) a \(\mathtt{SW2}\) - response return code (status word).

## Poznámka Anki 1739789300763

Karty Anki: 1739789300763
GUID: nxcw7)!;9^; štítky: ni-hwb::p01.

Metadata původního zdroje pro kartu 1739789300763: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Describe examples of smart card communication protocols. How are their data transmitted?

### Odpověď (Back)

Data of smart card communiation protocols are trasmitted inside trasmission protocol data units (TPDU). The most commonly used protocols include:

- \(\mathtt{T = 0}\) protocol - byte-oriented,

- \(\mathtt{T = 1}\) protocol - block-oriented.

## Poznámka Anki 1739789370649

Karty Anki: 1739789370650
GUID: MP]XsnkMwE; štítky: ni-hwb::p01.

Metadata původního zdroje pro kartu 1739789370650: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Describe the process of smart card initialization.

### Odpověď (Back)

Smart card initialization is split into the following phases:

- the terminal indicates the presence of the card,
- the terminal starts supplying power,
- the terminal starts the clock and reset signals,
- the cards responds with the answer to reset message,
- the terminal decodes the answer to reset,
- protocol parameters are chosen.

## Poznámka Anki 1739789922221

Karty Anki: 1739789922221
GUID: Nz#/Hy8s65; štítky: ni-hwb::p01.

Metadata původního zdroje pro kartu 1739789922221: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Compare the implementation of cryptographic functions using software and hardware modules.

### Odpověď (Back)

|       **software module** |       **hardware module** |         
|       easier implementation and development |       harder implementation and development |         
|       higher flexibility (possibility of updates) |       little to no flexibility |         
|       opennes (possibility of code audit)
 |       closedness (secret specification details) |         
|       lower secret data security (possibility of access through RAM)
 |       higher secret data security (tamper resistance) |          
|       harder to prove tampering
 |       easier to prove tampering (tamper evidence) |           
|       weakened by OS vulnerabilities, attacks or malware |       
 |

## Poznámka Anki 1739789963952

Karty Anki: 1739789963953
GUID: dG~UuySKFT; štítky: ni-hwb::p01.

Metadata původního zdroje pro kartu 1739789963953: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Describe the types of memory found on Java Cards.

### Odpověď (Back)

| 
      **persistant storage** | 
      **transient storage** | 

| 
      implemented using EEPROM | 
      implemented using RAM | 

| 
      capacity ~64 KB | 
      capacity ~1 KB | 

| 
      content persists after card ejection | 
      content is lost after card ejection | 

| 
      slower | 
      faster | 

| 
      worn out by repeated usage | 
 |

## Poznámka Anki 1739790332164

Karty Anki: 1739790332164
GUID: phctp:%zVi; štítky: ni-hwb::p01.

Metadata původního zdroje pro kartu 1739790332164: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Describe measures used against tampering.

### Odpověď (Back)

Measures used against tampering include the following:

- **tamper evidence** - the device manifests tampering attempts (seal),

- **tamper resistence** - the device is hard to tamper with (potting in resin),

- **tamper detection** - the device itself detects tampering attempts (light sensor).

- **tamper response** - the device itself performs actions upon being tampered with (memory erasure).

## Poznámka Anki 1739790434950

Karty Anki: 1739790434951
GUID: Mq!o$]<NX,; štítky: ni-hwb::p01.

Metadata původního zdroje pro kartu 1739790434951: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Describe a hardware security module (HSM).

### Odpověď (Back)

Hardware security module (HSM) is a physical device that supports the following functions:

- secure key generation,
- secure key storage,
- encryption and decryption,
- signing and verification of signatures,
- secure authentication,

- CPU offloading,
- SSL/TLS acceleration.

## Poznámka Anki 1739790501152

Karty Anki: 1739790501152
GUID: vHL$AZZQT=; štítky: ni-hwb::p01.

Metadata původního zdroje pro kartu 1739790501152: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

List examples of standards of security requirements for hardware security modules (HSM).

### Odpověď (Back)

Standards of security requirements for hardware security modules (HSM) include:

- FIPS 140 (NIST),
- Common Criteria for Information Technology Security Evaluation,
- FIPS 140-2.

## Poznámka Anki 1739790558754

Karty Anki: 1739790558754
GUID: js9{^kQ$Gs; štítky: ni-hwb::p01.

Metadata původního zdroje pro kartu 1739790558754: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Describe the levels of security requirements for hardware security modules (HSM) according to FIPS 140-2.

Popište jednotlivé úrovně požadavků na bezpečnost hardwarových bezpečnostních modulů (HSM) podle FIPS 140-2.

### Odpověď (Back)

FIPS 140-2 establishes the following levels of security requirements for hardware security modules (HSM):

- **level 1** - at least one approved algorithm of approved security function,

- **level 2 **- tamper evidence,

- **level 3** - tamper resistance,

- **level 4 **- higher temper resistance and resistance to environmental effects.

## Poznámka Anki 1739790854910

Karty Anki: 1739790854911
GUID: ldJgHU!;4O; štítky: ni-hwb::p01.

Metadata původního zdroje pro kartu 1739790854911: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Describe cryptographic hardware and the methods of its implementation.

### Odpověď (Back)

Cryptographic hardware is a type of hardware that is specialized for cryptohraphic operations which may be strenuous for the CPU. It provides support for symmetric ciphers (shifts, S-Box, operations in \(GF(2^8)\), etc.) and asymmetric ciphers (operations in \(GF(p)\), elliptic curve operations, modular exponentiation, etc.). Cryptographic hardware can be implemented as follows:

- specialized CPU execution unit,
- dedicated cryptographic core of the CPU,
- cryptographic coprocessor connected via a bus.

