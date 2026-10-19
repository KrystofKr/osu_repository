# NI-SBF – Přednáška 07

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/ni-sbf/NI-SBF.apkg; APKG SHA-256 eea8ecb13bdb56a02027b1cf6860588c0d4e44a6ec0b1d9b60c8cf7bc0df0806. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: e39cc77808ce484ac431215d36a50c128a0bf18ed66d8b544ffa1d5eb2a9d7be.
Původní balíčky: NI-SBF
Rozsah: 17 poznámek, 17 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1730900157801

Karty Anki: 1730900157801
GUID: Oi[T`c3XOj; štítky: ni-sbf::p07.

Metadata původního zdroje pro kartu 1730900157801: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Describe the difference between authentication and authorization.

### Odpověď (Back)

**Authentication** is the process of verifying a user's identity (e.g. using a password, key, or fingerprint). **Authorization**, on the other hand, is the process of veryfing whether a given user has sufficient permissions to carry out an action (e.g. using their identity, group mebership, or RBAC).

## Poznámka Anki 1730900343014

Karty Anki: 1730900343015
GUID: ra@)b1e1pD; štítky: ni-sbf::p07.

Metadata původního zdroje pro kartu 1730900343015: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

What is an authentication factor? What factor groups are there?

### Odpověď (Back)

An authentication factor is a piece of information used to authenticate an identity. There are three common factor groups:

- **knowledge** - something the user knows,

- **possesion** - something the user has,

- **inherence** - something the user is.

## Poznámka Anki 1730900496679

Karty Anki: 1730900496679
GUID: i*vG{6N`sm; štítky: ni-pb::21 ni-sbf::p07.

### Otázka (Front)

Describe additional authentication factors.

### Odpověď (Back)

Traditional authentication factors are often amended with the following additional factors:

- **behavior** - time and frequency of authentication requests,
- **location** - physical (IP, geolocation) or virtual (VPN, URL referrer).

## Poznámka Anki 1730900532960

Karty Anki: 1730900532960
GUID: vXRB7Y2>)3; štítky: ni-sbf::p07.

Metadata původního zdroje pro kartu 1730900532960: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Describe multi-factor authentication (MFA).

### Odpověď (Back)

Multi-factor authentication (MFA) is a type of authentication which uses two or more authentication factors.

## Poznámka Anki 1730901010088

Karty Anki: 1730901010088
GUID: eaX&^3<x&x; štítky: ni-pb::21 ni-sbf::p07.

Metadata původního zdroje pro kartu 1730901010088: modrý příznak autora: v poslední verzi upraveno.

### Otázka (Front)

Describe the phases of identity and access management (IAM).

### Odpověď (Back)

Identity and access management operates in the two following phases:

- **configuration phase** - registration of identity, provisioning of credentials, and authorization of access;

- **operation phase** - self-identification, authentication, and access control.

## Poznámka Anki 1730901253208

Karty Anki: 1730901253208
GUID: tbz4Q+[ip~; štítky: ni-sbf::p07.

Metadata původního zdroje pro kartu 1730901253208: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Define cryptographic salt.

### Odpověď (Back)

Cryptographic salt is a parameter that alters the outputs of cryptographic algorithms so that their results differ even in case the inputs are the same. This prevents attackers from reusing once cracked passwords multiple times.

## Poznámka Anki 1730902022008

Karty Anki: 1730902022008
GUID: sg0d{.nI%Y; štítky: ni-sbf::p07.

Metadata původního zdroje pro kartu 1730902022008: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Describe one-time password algorithms standardized by the Initiative for Open Authentication (OATH).

### Odpověď (Back)

The Initiative for Open Authentication (OATH) standardizes the following algorithms:

- **HMAC-based one-time password** (HOTP) - based on a counter:

\[\operatorname{HOTP}(\text{key}, \text{counter}) = \operatorname{truncate} \big( \operatorname{HMAC}_{\text{SHA-1}}(\text{key}, \text{counter}) \big),\]

- **time-based one-time password **(TOTP) - based on timestamps:

\[\operatorname{TOTP} \Big( \text{key}, \Big \lfloor \frac{\text{time} - \text{oldest time}}{\text{time step}} \Big \rfloor \Big) = \operatorname{HOTP} \Big (\text{key}, \Big \lfloor \frac{\text{time} - \text{oldest time}}{\text{time step}} \Big \rfloor \Big),\]

- **OATH challenge-response algorithm **(OCRA) - based on the exchange of challenge-response messages.

## Poznámka Anki 1730902686651

Karty Anki: 1730902686651
GUID: DJ1r3O($5j; štítky: ni-pb::21 ni-sbf::p07.

### Otázka (Front)

Describe Lamport's one-time password scheme (S/KEY)

### Odpověď (Back)

Lamport's one-time password scheme (S/KEY) begins with the client calculating a chain of hashes using a seed \(s_0\) and hash function \(h\) as follows:
\[\begin{matrix}
s_1 = h(s_0)\\
s_2 = h(s_1)\\
\vdots\\
s_n = h(s_{n - 1}).
\end{matrix}\]During enrollment, the client passes \(s_n\) to the server. The chain is then used in reverse order as when given \(s_{n - 1}\), the server can verify that
\[h(s_{n - 1}) = s_n.\]Once all the values in the chain are consumed, the client must choose a new seed.

## Poznámka Anki 1730902870263

Karty Anki: 1730902870263
GUID: E)0i@!hupY; štítky: ni-sbf::p07.

Metadata původního zdroje pro kartu 1730902870263: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Describe biometric authentication methods.

### Odpověď (Back)

Biometric authentication methods can be categorized as follows:

- **physiological **(visual) - body part similarities (face, fingerprint);

- **behavioral **(non-visual) - similarities in behavior (voice, signature).

## Poznámka Anki 1730903260629

Karty Anki: 1730903260629
GUID: fOCHS9`Tde; štítky: ni-sbf::p07.

Metadata původního zdroje pro kartu 1730903260629: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Describe the processing phases in biometric systems.

### Odpověď (Back)

Processing in biometric systems can be split into the following phases:

- **enrollment** - repeated measurement, reference value computation and secure storage;

- **recognition** - single measurement, comparison with the reference value.

The recognition phase can be further categorized as follows:

- **verification** - subject's identity is known prior to the biometric processing and only has to be verified;

- **identification** - subject's identity isn't known prior to the biometric processing and has to be retrieved.

## Poznámka Anki 1730903418326

Karty Anki: 1730903418326
GUID: JJK2{(.-%s; štítky: ni-sbf::p07.

Metadata původního zdroje pro kartu 1730903418326: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Describe the false acceptance rate (FAR) and false rejection rate (FRR) in biometric systems.

### Odpověď (Back)

**False acceptance rate **(FAR)** **is the frequency of cases in which the biometric system grants access to an unauthorized subject whereas **false rejection rate **(FRR) is the frequency of cases in which the biometric system denies access to an authorized subject.

## Poznámka Anki 1730903599367

Karty Anki: 1730903599367
GUID: Ljy[0vVcT-; štítky: ni-sbf::p07.

Metadata původního zdroje pro kartu 1730903599367: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Describe a harware security module (HSM).

### Odpověď (Back)

Hardware security module (HSM) is a physical device that supports the following functions:

- secure key generation,
- secure key storage,
- encryption and decryption,
- cryptographic signing and verification,
- secure authentication,
- CPU offloading,
- SSL/TLS acceleration.

## Poznámka Anki 1730903813522

Karty Anki: 1730903813522
GUID: k|oF?((Ko!; štítky: ni-pb::21 ni-sbf::p07.

### Otázka (Front)

Describe security measures used in hardware security modules (HSM).

### Odpověď (Back)

Hardware security modules (HSM) usually use the following security measures:

- **physical** - seals, light sensors;

- **logical** - integrity checks, secure firmware.

## Poznámka Anki 1730904469053

Karty Anki: 1730904469053
GUID: dE=aHV#/N7; štítky: ni-pb::21 ni-sbf::p07.

### Otázka (Front)

Describe measures used against tampering.

### Odpověď (Back)

Measures used against tampering include the following:

- tamper evidence,

- tamper resistence,

- tamper detection,

- tamper responsiveness.

## Poznámka Anki 1730904618397

Karty Anki: 1730904618397
GUID: b_a_jU}Ln.; štítky: ni-pb::21 ni-sbf::p07.

### Otázka (Front)

Describe the types of keys used in hardware security modules (HSM).

### Odpověď (Back)

Hardware security modules (HSM) typically use the following types of keys:

- **storage keys** - used to encrypt other stored keys,

- **transport keys** - used to encrypt keys during exchange,

- **functional keys** - used for cryptographic functions.

## Poznámka Anki 1730904819318

Karty Anki: 1730904819319
GUID: JM=(U%2Z#Y; štítky: ni-sbf::p07.

Metadata původního zdroje pro kartu 1730904819319: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Describe the levels of requirements for hardware security module (HSM) security according to FIPS 140-2.

### Odpověď (Back)

FIPS 140-2 specifies the following levels of requirements for hardware security modules (HSM):

- **level 1 **- at least one approved encryption algorithm or at least one approved security function;

- **level 2 **- tamper evidence;

- **level 3 **- better tamper evidence and tamper resistance;

- **level 4 **- high tamper evidence and resistance, resistance to environmental factors.

## Poznámka Anki 1734303192656

Karty Anki: 1734303192656
GUID: FqW-Home4l; štítky: ni-pb::21 ni-sbf::p07.

### Otázka (Front)

Describe key stretching (password stretching).

### Odpověď (Back)

Key stretching (password stretching) is a technique used to improve the resillience of a key or password to brute-force attacks by increasing the resources required to test each possible key or password. One way of achieving this is by repeatedly hashing the password or key until a required number of iterations is reached.

