# NI-HWB – Přednáška 03

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/ni-hwb/NI-HWB.apkg; APKG SHA-256 a65d26859a40bf4bc1c7dc8804425425d385ad2331d944e375f0fd10ce6e3550. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: ac319344d2de2cb4060d944b0c9d196f41ac858e59c961026ffe267a795b1399.
Původní balíčky: NI-HWB
Rozsah: 5 poznámek, 5 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1740996300889

Karty Anki: 1740996300889
GUID: c7%rx5-QNi; štítky: ni-hwb::p03.

Metadata původního zdroje pro kartu 1740996300889: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Describe a side-channel attack.

Popište útok postranním kanálem (side-channel attack).

### Odpověď (Back)

Side-channel attack is typically a passive non-invasive attack. It exploits information emitted by the target which is typically not a part of its main function. Side-channels typically abuse the weaknesses of:

- **algorithms** - may leak information in a suitable format (square-and-multiply),

- **architectures** - influence the timing and order of operations (Meltdown, Spectre),

- **technologies** - influence power consumption or emitted electromagnetic field.

## Poznámka Anki 1740996495635

Karty Anki: 1740996495635
GUID: Ib6Lc!XAM[; štítky: ni-hwb::p03.

Metadata původního zdroje pro kartu 1740996495635: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Describe the types of side-channel attacks.

### Odpověď (Back)

Side-channel attack types include:

- **timing **- duration of an operation depends on secret data (array comparison attack),

- **error** - error code depends on secret data (padding oracle),

- **power** - power consumption depends on secret data (simple power analysis, differential power analysis),

- **electromagnetic** - emitted electromagnetic field depends on secret data (TEMPEST).

## Poznámka Anki 1740997175174

Karty Anki: 1740997175174
GUID: o~179wcwOE; štítky: ni-hwb::p03.

Metadata původního zdroje pro kartu 1740997175174: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Describe the power side-channel attack on square and multiply.

### Odpověď (Back)

Power side-channel attack on square and multiply works by measuring the power consumption of the target device. The multiplication branch in square-and-multiply executes only if the bit at the given position in the exponent is set to 1. Therefore, the bits of the exponent are revealed through spikes in the power consumption of the device.

## Poznámka Anki 1741000346863

Karty Anki: 1741000346864
GUID: F&#rI0cs2a; štítky: ni-hwb::p03.

### Otázka (Front)

Describe the simple power analysis (SPA) side-channel attack on the Advanced Encryption Standard (AES).

### Odpověď (Back)

Simple power analysis (SPA) side-channel attack on the Advanced Encryption Standard (AES) targets the expanded key rather than the main encryption key. This is because the Hamming weights of the main key provide too little information. The expanded key can be divided into 4 parts each consisting of 5 bytes. The main idea is that these parts deterministically influence each other and these relations can be expressed using algebraic equations. Given a part \(P_i\) we can compute:

- 2 \(\texttt{SubBytes}\) results and 1 \(\texttt{Rcon}\) result used in \(P\),
- 4 bytes of \(P_{i + 1}\) and 1 \(\texttt{SubBytes}\) result used in \(P_{i + 1}\),
- 3 bytes of \(P_{i - 1}\) and 1 \(\texttt{SubBytes}\) result used in \(P_{i - 1}\),
- 2 bytes of \(P_{i - 2}\) and 1 \(\texttt{SubBytes}\) result used in \(P_{i - 2}\),
- 1 byte of \(P_{i-3}\) and 1 \(\texttt{SubBytes}\) result used in \(P_{i-3}\).

Including the 5 bytes of \(P_i\), this yields 22 bytes in total. The attack is then carried out as follows:

- measure the Hamming weight of all of the 22 bytes above;
- choose 5 bytes to be plugged as \(P_i\) that match the measured Hamming weights;
- compute the rest of the related bytes and check if their Hamming weights match the measured Hamming weights;
- if they all match, remember them as key candidates.

This process then gets repeated for all of the possible combinations of the 5 bytes. The more Hamming weights of the parts of the key expansion we are able to measure, the more we will be able to decrease the possible keyspace.

### Doplňující pole (Extra)

It is important to realize that there are multiple values of a byte that have a given Hamming weight (e.g. for Hamming weight of 1, we have 8 possible values). Inaccuracies in the measurement of the Hamming weights will further increase the key space.

## Poznámka Anki 1741000378787

Karty Anki: 1741000378787
GUID: s@$YpehmU@; štítky: ni-hwb::p03.

Metadata původního zdroje pro kartu 1741000378787: modrý příznak autora: v poslední verzi upraveno; v původním balíčku pozastavená karta.

### Otázka (Front)

Describe the key expansion in the Advanced Encryption Standard (AES).

Popište expanzi klíče AES.

### Odpověď (Back)

Suppose 32 bit words and the Advanced Encryption Standard (AES) cipher with key \(k\) consisting of \(N_k\) words. Next, suppose an array of words \(w\). First, copy \(k\) into \(w\) starting from its beginning. As a result, the elements \(w[0], \dots, w[N_k - 1]\) will be occupied. Then, \(w[i]\) can be computed as follows:

- Select the word at \(w[i - N_k]\). If \(|i|_{N_k} = 0\) apply \(\texttt{RotWord}\) (rotation of its bytes), \(\texttt{SubWord}\) (substitution of its bytes), and \(\texttt{Rcon}\) (multiplication of its bytes using a constant).
- Select the word at \(w[i - 1]\). If \(N_k > 6\) and \(|i|_{N_k} = 4\) apply \(\texttt{SubWord}\) (substitution of its bytes).
- XOR both selected words and store the result at \(w[i]\).

