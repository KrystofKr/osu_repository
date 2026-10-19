# NIE-BLO – Přednáška 01

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/nie-blo/NIE-BLO.apkg; APKG SHA-256 d675740a5d37d5b7b821ba3f30e724e22b0b39b082ab6be534fb2b3e252f014a. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: b1fbcd5286612e66242956e7ae484464865c6a0915d0e7ee68e8fc47bd0df05b.
Původní balíčky: NIE-BLO
Rozsah: 8 poznámek, 8 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1727431212726

Karty Anki: 1727431212727
GUID: ElZnVue%tk; štítky: nie-blo::p01.

Metadata původního zdroje pro kartu 1727431212727: v původním balíčku pozastavená karta.

### Otázka (Front)

Describe Bitcoin.

### Odpověď (Back)

Bitcoin is a decentralized cryptocurrency. It consists of a peer-to-peer network of cooperating nodes that listen for transactions, verify them, and publish them within a blockchain. Bitcoin uses digital signatures to verify the ownership of funds and a proof of work system (mining) to achieve consensus between the nodes (ruling out double spending).

## Poznámka Anki 1727431733768

Karty Anki: 1727431733768
GUID: l[|<9oCA+m; štítky: nie-blo::p01.

Metadata původního zdroje pro kartu 1727431733768: v původním balíčku pozastavená karta.

### Otázka (Front)

Describe the Bitcoin protocol.

### Odpověď (Back)

The Bitcoin protocol consists of the following steps:

- new transactions are broadcast by clients;
- nodes gather the transactions in a block;
- each node searches for a proof of work for the block being created;
- once any node finds the proof of work, it broadcasts the block in the network;
- other nodes accept this block only if all transactions in it are valid.

Nodes express their acceptance by creating another block on top of the accepted one using its hash.

## Poznámka Anki 1727432149727

Karty Anki: 1727432149727
GUID: nyY7kX8~Qs; štítky: nie-blo::p01.

Metadata původního zdroje pro kartu 1727432149727: v původním balíčku pozastavená karta.

### Otázka (Front)

Describe a Bitcoin wallet and address.

### Odpověď (Back)

**Bitcoin wallet** is a key pair consisting of a public key and a private key. **Bitcoin address** is an identifier that represents a destination for a bitcoin payment. It is generated from the public key of a wallet.

## Poznámka Anki 1727436197886

Karty Anki: 1727436197887
GUID: ibK,cA:XIJ; štítky: nie-blo::p01.

Metadata původního zdroje pro kartu 1727436197887: v původním balíčku pozastavená karta.

### Otázka (Front)

Describe a bitcoin transaction.

### Odpověď (Back)

Bitcoin transaction consists of the following:

- **hash **- hash of the current transaction,

- **inputs **- references to previous transactions that contain the spendable bitcoins:

- **previous transaction** - hash of a previous transaction,

- **signature **(\(\texttt{scriptSig}\)) - hash of the current transaction signed with the sender's private key,

- **outputs **- instructions for sending bitcoins:

- **value** - amount of spent bitcoins,

- **address **(\(\texttt{scriptPubKey}\)) - public key for the receiver's bitcoin address.

Thanks to the hashes in the inputs, the transactions are linked together and form a chain.

 [Obrázek: paste-4dc75973c4c2337a08b58bdf3c99a163ba10e65c.jpg; soubor je v media/ v doprovodném ZIP]

## Poznámka Anki 1727436574477

Karty Anki: 1727436574477
GUID: Q{T]&(-26A; štítky: nie-blo::p01.

Metadata původního zdroje pro kartu 1727436574477: v původním balíčku pozastavená karta.

### Otázka (Front)

Describe a bitcoin block.

### Odpověď (Back)

Bitcoin blocks aggregate transactions and form the nodes of a blockchain. The contents of a single block are as follows:

- **transactions** - list of transactions,

- **hash** - hash of the current block,

- **previous block** - hash of a previous block,

- **time** - creation time of the block,

- **target** - number determining the difficulty for the proof of work,

- **nonce** - number that serves as the proof of work.

## Poznámka Anki 1727436888473

Karty Anki: 1727436888473
GUID: p`#P]PYW2;; štítky: nie-blo::p01.

Metadata původního zdroje pro kartu 1727436888473: v původním balíčku pozastavená karta.

### Otázka (Front)

Describe bitcoin miners and proof of work.

### Odpověď (Back)

**Miners** are Bitcoin nodes that search for **proof of work** which is represented by a nonce such that the hash of the block containing the nonce is less than the value specified in the current target. If a miner finds such a nonce, it broadcasts the block and starts working on a new one. As a reward, they get to claim transaction fees and introduce new bitcoins via the coinbase transaction.

## Poznámka Anki 1727437239306

Karty Anki: 1727437239307
GUID: jjv;XD8/ZH; štítky: nie-blo::p01.

Metadata původního zdroje pro kartu 1727437239307: v původním balíčku pozastavená karta.

### Otázka (Front)

How does Bitcoin solve the problem of double spending?

### Odpověď (Back)

In order to prevent double spending, when a merchant receives a new transaction in a new valid block, they wait for a couple of next valid blocks being mined on top of the block in question for confirmation. In the case that there are multiple blocks coming from different miners, the merchant accepts the block that has the most blocks built on top of it and, therefore, has the most proof of work effort invested.

## Poznámka Anki 1727453263799

Karty Anki: 1727453263799
GUID: tMs{:4soFI; štítky: nie-blo::p01.

Metadata původního zdroje pro kartu 1727453263799: v původním balíčku pozastavená karta.

### Otázka (Front)

Describe the process of verification of a bitcoin transaction.

### Odpověď (Back)

The process of verification of a bitcoin transaction verifies that inputs of a transaction are authorized to collect the outputs of the referenced transaction. This is done using the two scripts inside a transaction:

- \(\texttt{scriptSig}\) from the input of the transaction,

- \(\texttt{scriptPubKey}\) from the output of the referenced transaction.

In this process the sender must provide:

- a public key, whose hash matches the destination of the referenced transaction,
- a signature to prove the ownership of the corresponding private key.

