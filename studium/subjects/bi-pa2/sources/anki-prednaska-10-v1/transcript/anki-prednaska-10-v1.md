# BI-PA2 – Přednáška 10

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::BI-PA2
Rozsah: 2 poznámek, 2 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1716820209892

Karty Anki: 1716820209892
GUID: b}Ub*EecZq; štítky: bi-pa2::p10 bi-spol::23.

### Otázka (Front)

Popište specifikaci a implementaci abstraktního datového typu.

### Odpověď (Back)

Abstraktní datový typ může být **specifikován**:

- **formálně** - signatury operací (syntaxe) a množina axiomů (sémantika),

- **neformálně** - signatury operací (syntaxe) a textový či obrázkový popis (sémantika).

Specifikace ADT však nemluví o jeho **implementaci**, která při dodržení syntaxe a sémantiky může být téměř libovolná. V C++ jsou ADT implementovány typicky za pomocí šablon tříd.

## Poznámka Anki 1716822514452

Karty Anki: 1716822514452
GUID: n8QZ;9$PZ_; štítky: bi-pa2::p10 bi-spol::23.

### Otázka (Front)

Popište prioritní frontu (priority queue).

### Odpověď (Back)

Prioritní fronta (queue) je asociativní abstraktní datový typ, který řadí prvky na základě jejich hodnoty (priority). Měla by podporovat následující operace:

- \(\mathtt{insert}\) - vloží prvek do fronty,

- \(\texttt{extract_min}\) - odebere libovolný prvek s nejnižší prioritou z fronty.

Očekávané časové složitosti těchto operací jsou \(\mathcal O(\log n)\), proto se prioritní fronta implementuje pomocí binární haldy.

