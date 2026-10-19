# NIE-BLO – Cvičení 06

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/nie-blo/NIE-BLO.apkg; APKG SHA-256 d675740a5d37d5b7b821ba3f30e724e22b0b39b082ab6be534fb2b3e252f014a. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: b1fbcd5286612e66242956e7ae484464865c6a0915d0e7ee68e8fc47bd0df05b.
Původní balíčky: NIE-BLO
Rozsah: 1 poznámek, 1 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1731062471040

Karty Anki: 1731062471050
GUID: trZ?aU~Sj*; štítky: nie-blo::c06.

Metadata původního zdroje pro kartu 1731062471050: v původním balíčku pozastavená karta.

### Otázka (Front)

Describe the reentrancy attack on Ethereum smart contracts.

### Odpověď (Back)

The reentrancy attack on Ethereum smart contracts is an attack that takes advantage of calls to external addresses. If the external call happens before the state of the contract is updated, the contract may be vulnerable to an reentrancy attack. This can be exploited for example as follows:

- the attacker uses a malicious contract to call \(\mathtt{withdraw}\) on the vulnerable contract,
- \(\mathtt{withdraw}\) uses an external call to transfer the Ether invoking \(\texttt{receive}\) on the malicious contract without first updating the state of the vulnerable contract,
- \(\texttt{receive}\) can now call \(\texttt{withdraw}\) again forming a loop draining the funds from the vulnerable contract without updating its state.

