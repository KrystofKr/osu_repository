# NI-REV – Cvičení 05

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/ni-rev/NI-REV.apkg; APKG SHA-256 9670f49b042e57cbd1c6d96f27c545d7e3e73f639dfdfaa5254dbc7ff55faa9f. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 7fc653b9bed751e297f56e0ab41b46bdc555bbf2270d66a69096723b55136e70.
Původní balíčky: NI-REV
Rozsah: 1 poznámek, 1 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1729798883459

Karty Anki: 1729798883459
GUID: BDG>~6c7j; štítky: ni-pb::12 ni-rev::c05.

### Otázka (Front)

Popište bázovou třídu (base class) v kontextu run-time type information (RTTI).

### Odpověď (Back)

Bázovou třídou (base class) vzhledem k odvozené třídě (derived class) v kontextu run-time type information (RTTI) rozumíme všechny třídy, místo kterých lze použít odvozenou třídu. Máme-li třídu\[\texttt{class D : public B_1, public B_2 \{} \dots \texttt{\};},\]pak budou vzhledem k \(\texttt D\) bázovými třídami třídy \(\texttt{B_1}\), \(\texttt{B_2}\) a třída \(\texttt D\) samotná.

### Doplňující pole (Extra)

Pokud bychom měli funkci, která přijímá referenci či ukazatel na některou z bázových tříd, tak takovou funkci můžeme zavolat s referencí či ukazatelem na odvozenou třídu.

