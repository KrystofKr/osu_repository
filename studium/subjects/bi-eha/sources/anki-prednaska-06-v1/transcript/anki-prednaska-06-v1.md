# BI-EHA – Přednáška 06

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-eha/BI-EHA.apkg; APKG SHA-256 c1faeda627c79eb61a7fd805476dd25213c149be4f50abfcbce04d85b2c27853. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 5c983498accbbf883eb18eb0e5351b8f14653c14dcca6e88ff363b189b4adf5b.
Původní balíčky: BI-EHA
Rozsah: 8 poznámek, 8 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1678450179707

Karty Anki: 1678450179707
GUID: i%N2ZbYp/0; štítky: bi-eha::p06 bi-ib::07 bi-ib::15 bi-ib::16 bi-ib::25.

### Otázka (Front)

What is privilege escalation? What types are there?

### Odpověď (Back)

Privilege escalation is the act of exploiting a security flaw in order to gain elevated access to resources that are normally protected. There are two types of privilege escalation:

- **horizontal** - gaining access to resources of another user with the same level of privilege,

- **vertical** - gaining access to resources of a more pivileged user.

## Poznámka Anki 1679646861423

Karty Anki: 1679646861423
GUID: d~~U[)[cP6; štítky: bi-eha::p06 bi-ib::18 bi-ib::25 ni-pb::21.

### Otázka (Front)

What is an authentication factor? What factor groups are there?

### Odpověď (Back)

An authentication factor is a piece of information used to authenticate an identity. There are three common factor groups:

- **knowledge** - something the user knows,

- **possesion** - something the user has,

- **inherence** - something the user is.

## Poznámka Anki 1679648504007

Karty Anki: 1679648504007
GUID: t![q$D>JML; štítky: bi-eha::p06.

### Otázka (Front)

What types of authentication attacks are there?

### Odpověď (Back)

The attacker can attempt to:

- **obtain plaintext credentials** (brute-force, dictionary attack, rainbow tables),

- **avoid entering credentials** (replay attack, authentication bypass).

## Poznámka Anki 1679649603464

Karty Anki: 1679649603464
GUID: fFvaX^]1;A; štítky: bi-eha::p06.

### Otázka (Front)

What is the difference between online and offline password cracking?

### Odpověď (Back)

**Online** password cracking means running an attack against a running process or remote system. It is inherently imited due to round-trip time. **Offline** password cracking entails computations on locally stored data and mainly consists of recovering passwords from stored hashes. It can leverage parallel processing.

## Poznámka Anki 1679650603020

Karty Anki: 1679650603020
GUID: f6rwu7V+Rc; štítky: bi-eha::p06.

### Otázka (Front)

What is password entropy?

### Odpověď (Back)

Password entropy is a measurement of the randomness or unpredictability of a password. It can usually be calculated as the number of bits it takes to effectively encode the password:
\[\log_2(L^N),\]where \(L\) is the number of all the possible characters in the password and \(N\) is its length.

## Poznámka Anki 1685798526950

Karty Anki: 1685798526950
GUID: nI9-0@X6G9; štítky: bi-eha::p06.

Metadata původního zdroje pro kartu 1685798526950: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

What is the difference between authentication and authorization?

### Odpověď (Back)

**Authentication** is the process of verifying the identity of an user. **Authorization** on the other hand, is the process of verifying whether a given user has sufficient permissions to execute a given operation.

## Poznámka Anki 1685799092437

Karty Anki: 1685799092437
GUID: MhPJ?1{aS1; štítky: bi-eha::p06 bi-ib::21.

### Otázka (Front)

What is the difference between a brute-force attack and a dictionary attack?

### Odpověď (Back)

A **brute-force attack** is a method that involves exhaustive systematic checking of all possible combinations of characters. However, these combinations may be limited by password policy. A **dictionary attack** is a more targeted approach that utilizes a pre-constructed list of possible passwords which is called a wordlist.

## Poznámka Anki 1685799280722

Karty Anki: 1685799280723
GUID: Q?)4,-6|^L; štítky: bi-eha::p06.

### Otázka (Front)

Describe rainbow tables?

### Odpověď (Back)

Rainbow tables are precomputed tables for caching the outputs of a hash function that are usually used for cracking password hashes. While taking up more storage they use much less processing time than a normal brute-force attack.

