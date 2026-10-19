# BI-PA1 – Přednáška 07

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::BI-PA1
Rozsah: 1 poznámek, 1 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1718548827661

Karty Anki: 1718548827661
GUID: lJZ.gpYf2A; štítky: bi-pa1::p07 bi-spol::19.

### Otázka (Front)

Popište ukazatel (pointer), operace s ním spjaté a jeho využití.

### Odpověď (Back)

Ukazatel (pointer) je datový typ představující odkaz na objekt programovacího jazyka, který se používá jako abstrakce adresy. S ukazatelem se pojí operátory:

- **address-of** (reference) - získá adresu daného objektu

\[\texttt{ T *x_ptr = &x;}\]

- **indirection** (dereference) - přistoupí k objektu odkazovanému ukazatelem

\[\texttt{T y = *x_ptr;}\]

Speciální hodnotou ukazatele je \(\texttt{nullptr}\), která vyjadřuje „prázdný“ ukazatel. Ukazatele jsou využívány při:

- předávání výstupních parametrů funkcím,
- předávání objektů, jejichž kopírování je náročné, jako parametry funkcí,
- přístupu k dynamicky alokovaným objektům.

