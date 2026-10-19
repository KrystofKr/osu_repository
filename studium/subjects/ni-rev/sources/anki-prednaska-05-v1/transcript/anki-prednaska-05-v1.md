# NI-REV – Přednáška 05

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/ni-rev/NI-REV.apkg; APKG SHA-256 9670f49b042e57cbd1c6d96f27c545d7e3e73f639dfdfaa5254dbc7ff55faa9f. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 7fc653b9bed751e297f56e0ab41b46bdc555bbf2270d66a69096723b55136e70.
Původní balíčky: NI-REV
Rozsah: 2 poznámek, 2 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1732205509973

Karty Anki: 1732205509973
GUID: x`BI++r%ZW; štítky: ni-rev::p05.

### Otázka (Front)

Popište postup pro rozpoznávání kompilátorů.

### Odpověď (Back)

Kompilátory lze rozpoznat pomocí:

- stylu kompilátoru (např. preferované instrukce),
- linkovaných runtime knihoven,
- formátu dekorovaných jmen.

## Poznámka Anki 1732205676421

Karty Anki: 1732205676421
GUID: fae>F@3+Y;; štítky: ni-rev::p05.

### Otázka (Front)

Popište postup pro rozpoznávání knihoven.

### Odpověď (Back)

Při rozpoznávání knihoven se přístup liší podle toho, zda je knihovna linkována dynamicky nebo staticky. Pro dynamické knihovny lze použít nástroje jako \(\texttt{dumpbin}\) nebo \(\texttt{CFF Explorer}\). V případě statických knihoven se typicky používají:

- signatury funkcí (několik prvních bytů),
- řetezce (copyright, verze, chybová hlášení).

