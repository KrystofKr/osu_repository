# BI-OSY – Přednáška 01

Původ: FIT ČVUT Anki, /mnt/c/Users/kryst/Desktop/One drive-local/fit-cvut-anki-master/fit-cvut-anki-master/fit-cvut-anki-master/bi-osy/BI-OSY.apkg; APKG SHA-256 e601d54cae58e1923ab743a64796ef89ec49f6bcd52ac062288890242af207fc. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:26:38+02:00. Původní kolekce SHA-256: b95b42cacacaa5de70f8162d09b00582086c2fd5b59f3a299e3fc9531a688ab6.
Původní balíčky: BI-OSY
Rozsah: 6 poznámek, 6 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

Příznaky a pozastavení patří autorovi zdroje, nikoli studijnímu postupu uživatele. Dle README: červená = chyba nebo kontrola, oranžová = určeno k odstranění, zelená = duplicita, modrá = poslední úprava. Tyto karty zůstaly zachované a označené.

## Poznámka Anki 1678180240498

Karty Anki: 1678180240498
GUID: o;|);^|q*@; štítky: bi-osy::p01.

Metadata původního zdroje pro kartu 1678180240498: v původním balíčku pozastavená karta.

### Otázka (Front)

Porovnejte hyper-threading a multi-threading.

### Odpověď (Back)

| 
      **hyper-threading**
 | 
      **multi-threading**
 | 

| 
      používá se v některých Intel procesorech
 | 
      používá se v UltraSPARC T procesorech
 | 

| 
      kritické části jádra jsou duplikovány a jádro tak může zpracovávat dva instrukční proudy (vlákna)
 | 
      části každého jádra jsou zdvojeny, jádro může zpracovávat \(2 \times 4\) instrukčních proudů (vláken)
 |

## Poznámka Anki 1678180456136

Karty Anki: 1678180456136
GUID: D~|dPQY6y;; štítky: bi-ib::25 bi-osy::p01.

### Otázka (Front)

Co je to operační systém? Jaké jsou jeho úlohy?

### Odpověď (Back)

OS je základní SW, který funguje jako prostředník mezi HW a aplikacemi nebo uživateli. Mezi jeho úlohy patří:

- **správa a sdílení prostředků** - procesor, paměť, uživatelská konta, soubory,

- **poskytování rozhraní** **aplikacím i uživatelům** - Win32 API, ale také CLI a GUI.

## Poznámka Anki 1687704017170

Karty Anki: 1687704017188
GUID: d*gEs;2ip{; štítky: bi-osy::p01.

Metadata původního zdroje pro kartu 1687704017188: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Porovnejte CISC a RISC.

### Odpověď (Back)

| 
      **Complex Instruction Set Computer** | 
      **Reduced Instruction Set Computer** | 

| 
      obvykle větší počet instrukcí | 
      obvykle menší počet instrukcí | 

| 
      instrukce různé délky (1B-13B) | 
      jedna nebo dvě délky instrukcí (2B, 4B) | 

| 
      obvykle mnoho adresních módů | 
      obvykle méně jednodušších adresních módů |

## Poznámka Anki 1687704382933

Karty Anki: 1687704382933
GUID: LzD#HkF,E*; štítky: bi-osy::p01.

Metadata původního zdroje pro kartu 1687704382933: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Jaké jsou typické stupně zřetězeného zpracování instrukcí?

### Odpověď (Back)

Při zřetězeném zpracování instrukcí, jako např. u RISC ISA (3, 0), můžeme zpracování instrukce rozdělit do následujících stupňů:

- instruction fetch (IF),
- instruction decode and operand fetch (ID/OF),
- execute (EX),
- memory access (MEM),
- write back (WB).

## Poznámka Anki 1687704672599

Karty Anki: 1687704672599
GUID: qTI])2wA{q; štítky: bi-osy::p01.

Metadata původního zdroje pro kartu 1687704672599: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Definujte přerušení.

### Odpověď (Back)

Přerušení (interrupt) je asynchronní nebo synchronní událost či požadavek na CPU jádro, aby přerušilo právě vykonávaný program a promptně reagovalo na příčinu této události.

## Poznámka Anki 1687705034171

Karty Anki: 1687705034172
GUID: c^S50#kYh%; štítky: bi-osy::p01.

Metadata původního zdroje pro kartu 1687705034172: zelený příznak autora: duplicita; v původním balíčku pozastavená karta.

### Otázka (Front)

Co je to systémové volání?

### Odpověď (Back)

Systémové volání je způsob, kterým si neprivilegovaný program běžící v user mode může požádat o poskytnutí služby od operačního systému. Systémové volání probíhá stejně jako běžné volání rutiny.

