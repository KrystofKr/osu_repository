# BI-BEK – Přednáška 05

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-bek/BI-BEK.apkg; APKG SHA-256 8b1a9f700cf93cf99c030811606998d3d282ec99cc7d73e806af320f264d4ea6. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 735709f33719335ca8dfc56a2c567cb9b621f1f50f3818756a9e3f4fd0fc9380.
Původní balíčky: BI-BEK
Rozsah: 4 poznámek, 4 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1680121255113

Karty Anki: 1680121255113
GUID: C|]DAvx|Tq; štítky: bi-bek::p05 bi-ib::08.

### Otázka (Front)

Uveďte doporučení pro psaní bezpečnějšího kódu v C.

### Odpověď (Back)

Pro bezpečnější kód se doporučuje:

- vyhnout se nebezpečným funkcím jako např. \(\mathtt{strcpy}\), \(\mathtt{strcat}\), \(\mathtt{sprintf}\), \(\mathtt{gets}\);
- používat ochranu zásobníku;
- psát testy;
- provádět statickou a dynamickou analýzu kódu.

## Poznámka Anki 1680121379488

Karty Anki: 1680121379488
GUID: i(<-D<.pE; štítky: bi-bek::p05 bi-ib::08.

### Otázka (Front)

Jaký je rozdíl mezi statickou a dynamickou analýzou kódu?

### Odpověď (Back)

Statická analýza je prováděna na zdrojovém kódu, tedy program neběží. Naproti tomu dynamická analýza je spouštěna na běžícím programu.

## Poznámka Anki 1680121507511

Karty Anki: 1680121507511
GUID: A&,W]:v5&W; štítky: bi-bek::p05 bi-ib::08.

### Otázka (Front)

Jak funguje Guard Malloc (\(\mathtt{libgmalloc}\))?

### Odpověď (Back)

Předpokládejme buffer na haldě, u nějž chceme zjistit případné přetečení. Guard Malloc nahradí veškeré funkce pro práci s pamětí pomocí preloadu. Při alokaci nového datového bloku se potom alkokuje celá paměťová stránka a blok se umístí na její konec. Stránka bezprostředně za ní se označí jako nepřístupná. Přístup za konec bufferu potom automaticky vyvolá procesorovou výjimku.

## Poznámka Anki 1717602260167

Karty Anki: 1717602260167
GUID: Ay&-JG2^YX; štítky: bi-bek::p05 bi-ib::08.

### Otázka (Front)

Popište příčiny typických chyb v C/C++.

### Odpověď (Back)

Mezi příčiny typických chyb v C/C++ patří:

- **funkce pro práci s řetězci** - buffer overflow, chyby formátovacích řetězců;

- **převody a práce s multi-byte a Unicode řetězci** - buffer overflow;
- **přetečení datových typů** - obcházení logiky programu (např. testování mezí).

