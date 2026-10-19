# BI-EHA – Přednáška 08

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-eha/BI-EHA.apkg; APKG SHA-256 c1faeda627c79eb61a7fd805476dd25213c149be4f50abfcbce04d85b2c27853. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 5c983498accbbf883eb18eb0e5351b8f14653c14dcca6e88ff363b189b4adf5b.
Původní balíčky: BI-EHA
Rozsah: 8 poznámek, 8 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1682065068945

Karty Anki: 1682065068945
GUID: x.)%NEz^5`; štítky: bi-eha::p08 bi-ib::13.

### Otázka (Front)

List examples of Wi-Fi management frames and their uses.

### Odpověď (Back)

Some examples of Wi-Fi management frames are:

- **association request** - a station requests to join a BSS via an AP,
- **probe request** - a station queries other active stations and APs on a frequency,

- **beacon **- an AP advertises an SSID.

## Poznámka Anki 1682065321027

Karty Anki: 1682065321027
GUID: CC],+]_$Y(; štítky: bi-eha::p08 bi-ib::13.

### Otázka (Front)

What does BSS, SSID, ESS and ESSID stand for?

### Odpověď (Back)

The abbreviations stand for the following:

- **Basic Service Set **(BSS) - a group of devices that are connected to the same AP,
- **Service Set Identifier** (SSID) - an unique string identifying an AP,

- **Extended Service Set** (ESS) - a group of APs and their users belonging to the same service set,

- **Extended Service Set Identifier** (ESSID) - an unique string identifying the APs that belong in an ESS.

## Poznámka Anki 1682065850819

Karty Anki: 1682065850819
GUID: y{u[-P1Ye^; štítky: bi-eha::p08 bi-ib::13.

### Otázka (Front)

Describe Wired Equivalent Privacy (WEP).

### Odpověď (Back)

Wired Equivalent Privacy (WEP) is an obsolete security algorithm for Wi-Fi networks that uses the RC4 cipher and CRC32. The authentication process is as follows:

- The station sends an authentication request to the AP.
- The AP replies with a plaintext challenge.
- The station encrypts the challenge using a pre-shared key and sends it back.
- The AP decrypts the response and if it matches the challenge text, the station is allowed to connect.

## Poznámka Anki 1682080078840

Karty Anki: 1682080078840
GUID: Q6_f$G.6>A; štítky: bi-eha::p08 bi-ib::13.

### Otázka (Front)

Describe Wi-Fi Protected Access 2 (WPA2).

### Odpověď (Back)

Wi-Fi Protected Access (WPA) is a security algorithm for Wi-Fi networks. It is based on AES with CTR and CBC-MAC modes. Before the authentication process starts, both the station an the AP have to be in possesion of **pairwise master key** (PMK) - in the context of WPA-Personal this is the pre-shared key. Then the authentication process is as follows:

1. The AP sends an **ANONCE** value (a random value that the AP produced).
2. The station generates a **SNONCE **value and derives the **pairwise transit key** (PTK).
3. The station sends a **SNONCE** value and a **MIC** (Message Integrity Code). From now on all messages contain a MIC.
4. The AP derives its own PTK.
5. The AP sends an encrypted **group transit key** (GTK) and instructs the station to install the keys.
6. The station installs the keys and sends back a confirmation.

## Poznámka Anki 1682080260947

Karty Anki: 1682080260947
GUID: zDl99r6MzG; štítky: bi-eha::p08 bi-ib::13.

### Otázka (Front)

What is the difference between WPA-Personal and WPA-Enterprise?

### Odpověď (Back)

WPA-Personal uses a pre-shared key as the **pairwise master key** (PMK). In contrast to that, when using WPA-Enterprise the PMK is pulled from an external server (such as a radius server) following an authentiaction process.

## Poznámka Anki 1682102472853

Karty Anki: 1682102472854
GUID: C{}NR}0<@V; štítky: bi-eha::p08 bi-ib::13.

### Otázka (Front)

From which parameters is the pairwise transit key (PTK) derived?

### Odpověď (Back)

PTK is derived from:

- pairwise master key (PMK),
- ANONCE,
- SNONCE,
- MAC address of the AP,
- MAC addres of the station.

## Poznámka Anki 1685906425523

Karty Anki: 1685906425524
GUID: Ey!:IM+X:N; štítky: bi-eha::p08 bi-ib::13.

### Otázka (Front)

How can Wired Equivalent Privacy (WEP) be cracked?

### Odpověď (Back)

Because WEP uses RC4, a stream cipher, the same keystream must never be used twice. For this reason, WEP uses a 24-bit initialization vector, which is transmitted as plaintext. However, due to the limited keyspace WEP often reuses IVs. In as little as few minutes (on a busy network) an attacker can capture IV collisions and recover the key using statistical analysis.

## Poznámka Anki 1685907117073

Karty Anki: 1685907117073
GUID: y2T}Q;dmcp; štítky: bi-eha::p08 bi-ib::13.

### Otázka (Front)

What are some weaknesses of Wi-Fi Protected Access (WPA)?

### Odpověď (Back)

Wi-Fi Protected Access (WPA) has the following weaknesses:

- weak pre-shared keys are vulnerable to dictionary attacks,
- rainbow tables for most used SSIDs,
- weak WPS (Wi-Fi Protected Setup) PINs and implementation flaws,
- Dragonblood attack - downgrade and side-channel attack,
- KRACK (Key Reinstallation Attack).

