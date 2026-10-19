# BI-APS – Přednáška 02

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-aps/BI-APS.apkg; APKG SHA-256 63bfc5aa0323444676cf487a912504fe349947379582defbd46142eba140a34c. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 915a4d48ed325abbebd5302b61e301302fef124158fff2eaaa20c5a2a12f71ce.
Původní balíčky: BI-APS
Rozsah: 7 poznámek, 7 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1664217502402

Karty Anki: 1664217502403
GUID: v+{:<ua^`u; štítky: bi-aps::p02.

Metadata původního zdroje pro kartu 1664217502403: v původním balíčku pozastavená karta.

### Otázka (Front)

Jaké HDL (Hardware Description Language) známe?

### Odpověď (Back)

- VHDL (VHSIC Hardware Description Language; VHSIC - Very High Speed Integrated Circuits)
- Verilog a SystemVerilog

## Poznámka Anki 1664217666835

Karty Anki: 1664217666835
GUID: 6;/1.vtEg; štítky: bi-aps::p02.

Metadata původního zdroje pro kartu 1664217666835: v původním balíčku pozastavená karta.

### Otázka (Front)

Na jakých úrovních abstrakce lze ve Verilogu popsat obvod?

### Odpověď (Back)

- switch level (tranzistory)
- gate level (logická hradla)
- register transfer level (booleovské funkce)
- algorithmic level (high-level konstrukce jako \(\mathtt{if}\), \(\mathtt{else}\), \(\mathtt{for}\) a podobně)

## Poznámka Anki 1664217755743

Karty Anki: 1664217755743
GUID: wxoF&WXl8&; štítky: bi-aps::p02.

Metadata původního zdroje pro kartu 1664217755743: v původním balíčku pozastavená karta.

### Otázka (Front)

Charakterizujte strukturální popis obvodů v jazyce Verilog.

### Odpověď (Back)

Popisujeme, jak je obvod sestaven uvnitř, tedy vzájemné propojení vnitřních částí (modulů).

## Poznámka Anki 1664217774381

Karty Anki: 1664217774381
GUID: b#kDL>XNeN; štítky: bi-aps::p02.

Metadata původního zdroje pro kartu 1664217774381: v původním balíčku pozastavená karta.

### Otázka (Front)

Charakterizujte behaviorální popis obvodů v jazyce Verilog.

### Odpověď (Back)

Popisujeme, jak se obvod chová navenek. Primárně nás nezajímá, jak
bude obvod syntetizovaný. Popisujeme závislost výstupů na vstupech,
příp. stavových proměnných.

## Poznámka Anki 1664217866483

Karty Anki: 1664217866483
GUID: FAr;V]EbO/; štítky: bi-aps::p02.

Metadata původního zdroje pro kartu 1664217866483: v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte přiřazení. Jaké formy přiřazení rozlišujeme?

### Odpověď (Back)

Přiřazení je předpis, který přiřadí hodnotu výrazu na pravé straně přirazení do proměnné nebo vodiče na levé straně přiřazení. Rozlišujeme

- kontinuální přiřazení,
- procedurální přiřazení.

## Poznámka Anki 1664217913519

Karty Anki: 1664217913519
GUID: t$FF&k6Po3; štítky: bi-aps::p02.

Metadata původního zdroje pro kartu 1664217913519: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište kontinuální přiřazení.

### Odpověď (Back)

Kontinuální přiřazení přiřazuje hodnoty vodičům. Jsou vyhodnocena a aktualizována, kdykoliv
vstupní operandy (vodiče či proměnné) na pravé straně výrazu
změní hodnotu. Uvádí se klíčovým slovem \(\mathtt{assign}\).

## Poznámka Anki 1664218117753

Karty Anki: 1664218117754
GUID: C!K|]M}*xg; štítky: bi-aps::p02.

Metadata původního zdroje pro kartu 1664218117754: v původním balíčku pozastavená karta.

### Otázka (Front)

Popište procedurální přiřazení. Jaké rozlišujeme typy?

### Odpověď (Back)

Procedurální přiřazení přiřazuje hodnoty proměnným. Každé přiřazení uvnitř procedurální konstrukce je procedurální a na jeho levé straně musí být proměnná. Rozlišujeme

- blokující procedurální přiřazení (\(\mathtt =\)) - vyhodnocováno sekvenčně,
- neblokující procedurální přiřazení (\(\mathtt{<=}\)) - vyhodnocováno paralelně.

