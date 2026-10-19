# NI-REV – Přednáška 03

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/ni-rev/NI-REV.apkg; APKG SHA-256 9670f49b042e57cbd1c6d96f27c545d7e3e73f639dfdfaa5254dbc7ff55faa9f. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 7fc653b9bed751e297f56e0ab41b46bdc555bbf2270d66a69096723b55136e70.
Původní balíčky: NI-REV
Rozsah: 4 poznámek, 4 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1729762304713

Karty Anki: 1729762304713
GUID: zpEg5$-N3|; štítky: ni-pb::12 ni-rev::p03.

### Otázka (Front)

Popište postup určení velikosti struktury při reverzní analýze.

### Odpověď (Back)

Postup určení velikosti struktury je závislý na tom, kde se struktura nachází:

- **na zásobníku** - komplikované, velikost struktury bude součástí prostoru alokovaného pro lokální proměnné;

- **na haldě** - velikost struktury bude předávána funkci \(\texttt{malloc}\) (nebo jiné alokační funkci).

Případně může být zřejmá z práce se strukturou (např. při iteraci přes pole struktur).

## Poznámka Anki 1729764628709

Karty Anki: 1729764628710
GUID: P2Wpb?kEck; štítky: ni-pb::12 ni-rev::p03.

### Otázka (Front)

Popište reverzní analýzu polymorfní třídy s virtuálními metodami.

### Odpověď (Back)

Polymorfní třída s virtuálními metodami bude jako první prvek své paměťové reprezentace obsahovat ukazatel na tabulku virtuálních metod (VMT). Pokud daná třída některé virtuální metody neimplementuje, bude na jejich pozici ve VMT ležet adresa funkce \(\texttt{_purecall}\), která volání takové metody ošetří. V případě, že třída dědí z vícero tříd, budě dědit vícero VMT. V paměti pak bude uložena následovně:

- ukazatel na VMT první třídy,
- data první třídy,
- ukazatel na VMT druhé třídy,
- data druhé třídy,

atd.

## Poznámka Anki 1729765676405

Karty Anki: 1729765676405
GUID: mfOI{<=><F; štítky: ni-pb::12 ni-rev::p03.

### Otázka (Front)

Popište využití tabulky virtuálních metod (VMT) při reverzní analýze.

### Odpověď (Back)

Při reverzní analýze lze tabulku virtuálních metod (VMT) použít následovně:

- **nalezení typu objektu** - porovnáním jeho ukazatele na VMT se známými ukazateli na VMT,
- **nalezení dedičnosti** - prozkoumáním ukazatelů v paměti objektu a hledáním ukazatelů na VMT,

- **nalezení kódu objektu** - prozkoumáním ukazazelů v každé VMT.

## Poznámka Anki 1729800295111

Karty Anki: 1729800295111
GUID: Bz7i8h.+3; štítky: ni-pb::12 ni-rev::p03.

### Otázka (Front)

Popište run-time type information (RTTI) v kontextu reverzní analýzy. Jakým způsobem lze rekonstruovat třídní hierarchii programu?

### Odpověď (Back)

Run-time type information (RTTI) bude v programu dostupné pouze pokud program využívá funkcionality, které ji vyžadují (např. \(\texttt{dynamic_cast}\) nebo \(\texttt{typeid}\)). Na platformě MSVC je RTTI realizováno řadou struktur, mezi které patří:

- \(\texttt{_RTTITypeDescriptor}\) - obsahuje dekorované jméno třídy;

- \(\texttt{_RTTICompleteObjectLocator}\) - ukazatel na něj leží těsně před VMT a obsahuje odkazy na \(\texttt{_RTTITypeDescriptor}\) a \(\texttt{_RTTIClassHierarchyDescriptor}\);

- \(\texttt{_RTTIClassHierarchyDescriptor}\) - obsahuje informace o typu dědičnosti (např. zda je vícenásobná), počet bázových tříd (base classes) a jejich seznam.

Právě z počtu bázových tříd dokážeme rekonstruovat třídní hierarchii programu.

