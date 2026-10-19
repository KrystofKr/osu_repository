# BI-APS – Přednáška 04

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-aps/BI-APS.apkg; APKG SHA-256 63bfc5aa0323444676cf487a912504fe349947379582defbd46142eba140a34c. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: 915a4d48ed325abbebd5302b61e301302fef124158fff2eaaa20c5a2a12f71ce.
Původní balíčky: BI-APS
Rozsah: 6 poznámek, 6 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1665425530601

Karty Anki: 1665425530601
GUID: Ial!`K0pae; štítky: bi-aps::p04 bi-ib::04.

### Otázka (Front)

Jaké jsou typické stupně zřetězeného zpracování instrukcí?

### Odpověď (Back)

Při zřetězeném zpracování instrukcí, jako např. u RISC ISA (3, 0), můžeme zpracování instrukce rozdělit do následujících stupňů:

- instruction fetch (IF),
- instruction decode and operand fetch (ID/OF),
- execute (EX),
- memory access (MEM),
- write back (WB).

## Poznámka Anki 1665425601596

Karty Anki: 1665425601596
GUID: os<tl^U-~}; štítky: bi-aps::p04 bi-ib::04.

### Otázka (Front)

Jak realizujeme rozdělení procesu vykonávání instrukcí?

### Odpověď (Back)

Mezi jednotlivé stupně zařadíme v návrhu mezistupňové registry.

## Poznámka Anki 1665425917393

Karty Anki: 1665425917393
GUID: jiJq|CayT*; štítky: bi-aps::p04 bi-ib::04.

### Otázka (Front)

Co je to hazard u instrukčního zřetězení a jaké typy rozeznáváme?

### Odpověď (Back)

Hazard je konflikt při přístupu ke sdílenému prostředku, což je prostředek, který je opakovně použit ve více stupních instrukčního zřetězení.
**Typy**:

- datové (důsledek datových závislostí)
- řídící (instrukce měnící PC, tudíž obsah fronty instrukcí)
- strukturální (počet současných požadavků na daný prostředek převyšuje počet jeho instancí)

## Poznámka Anki 1665426091768

Karty Anki: 1665426091768
GUID: ieZgC3S3!(; štítky: bi-aps::p04.

Metadata původního zdroje pro kartu 1665426091768: v původním balíčku pozastavená karta.

### Otázka (Front)

Jak lze řešit datové hazardy?

### Odpověď (Back)

Datové hazardy lze řešit dvojím způsobem:

- **přeposílání **(forwarding) - výsledek vzniká dříve nebo ve stejném cyklu, jako ho má pozdější instrukce použít;

- **pozastavení **(stall) - pozdější instrukce potřebují výsledek dříve, než skutečně vznikne.

## Poznámka Anki 1665426256856

Karty Anki: 1665426256856
GUID: nnj[S>]*^0; štítky: bi-aps::p04 bi-ib::04.

Metadata původního zdroje pro kartu 1665426256856: v původním balíčku pozastavená karta.

### Otázka (Front)

Jak řešíme řídící hazardy?

### Odpověď (Back)

- **vyprázdnění (flush)** - instrukce čekající ve frontě odebereme resetováním mezistupňových registrů

- preventivně pomocí **předpovídání skoků**

## Poznámka Anki 1665426336138

Karty Anki: 1665426336138
GUID: sYtL>sfE*J; štítky: bi-aps::p04.

Metadata původního zdroje pro kartu 1665426336138: v původním balíčku pozastavená karta.

### Otázka (Front)

Jak řešíme strukturální hazardy?

### Odpověď (Back)

- **pozastavením (stall)** - upřednostníme jeden přístup před jiným
- zavedením vyšší **redundance **sdílených prostředků

