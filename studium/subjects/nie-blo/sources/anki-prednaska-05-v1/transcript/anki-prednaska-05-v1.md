# NIE-BLO – Přednáška 05

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/nie-blo/NIE-BLO.apkg; APKG SHA-256 d675740a5d37d5b7b821ba3f30e724e22b0b39b082ab6be534fb2b3e252f014a. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: b1fbcd5286612e66242956e7ae484464865c6a0915d0e7ee68e8fc47bd0df05b.
Původní balíčky: NIE-BLO
Rozsah: 2 poznámek, 2 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1729866321349

Karty Anki: 1729866321349
GUID: l?+OiZ@hk); štítky: nie-blo::p05.

Metadata původního zdroje pro kartu 1729866321349: v původním balíčku pozastavená karta.

### Otázka (Front)

Describe Ethereum gas.

### Odpověď (Back)

Ethereum gas is a unit for measuring computational and storage requirements that is converted to Ether using the gas free ratio. Its main use is to prevent denial-of-service (DoS) attacks that could be possible due to the fact that Ethereum provides a Turing-complete programming language. The gas cost of a transaction is made up of the following:

- **intrinsic cost** - flat fee for executing a transaction, burned during execution;

- **tip** - incentivizes miners/validators to prioritize the transaction, awarded to the miners/validators.

Additionaly, transactions that deploy smart contracts must pay for each opcode used in their bytecode.

## Poznámka Anki 1731525317302

Karty Anki: 1731525317302
GUID: s7E+GA+TEm; štítky: nie-blo::p05.

Metadata původního zdroje pro kartu 1731525317302: v původním balíčku pozastavená karta.

### Otázka (Front)

Describe a state transition of the Ethereum virtual machine (EVM)

### Odpověď (Back)

Ethereum virtual machine (EVM) transitions to a new state every time a block is appended to the blockchain. This process consists of the following phases:

- **pre-execution validation** - block header and structure verification,
- **initial state verification** - balance and nonce verification;

- **transaction execution loop **- signature verification, gas calculation, code execution;

- **post-execution validation** - header verification.

