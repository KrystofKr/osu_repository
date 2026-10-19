# BI-ZUM – 15 vyrokova logika SAT

Původ: místní Anki, profil User 1. Jde o export kartiček, nikoli ověřené znění učebnice.
Verze exportu: 2026-10-17T16:00:56+02:00. Původní kolekce SHA-256: 0d1f9aa982a5c3eaa31cfd838f48afceda879ae758526167d718d7f2d6347255.
Původní balíčky: before OSU::5 BI-ZUM
Rozsah: 5 poznámek, 5 karet.
ZIP zachovává přesná pole HTML, identifikátory, štítky, šablony a přiložená média.
Matematický zápis je zachovaný; před výukou vzorců, tabulek a obrázků ověřit originál vizuálně.
Existující odpovědi a případné chyby jsou obsahem zdroje; nepředstavují ověření znalostí studenta.

## Poznámka Anki 1785298610669

Karty Anki: 1785298610669
GUID: GNYnNz6qnY; štítky: AI_combined::15_vyrokova_logika_SAT iterace_11 src_773-775.

### Otázka (Front)

Jaký je rozdíl mezi syntaxí a sémantikou výrokové logiky a jak vznikají formule?

### Odpověď (Back)

**Syntax** určuje dobře utvořené formule: každá výroková proměnná je formule a aplikace povolených spojek (např. ¬, ∧, ∨, ⇒, ⇔, ⊕) na již vytvořené formule vytváří formule nové. **Sémantika** přiřazuje proměnným pravdivostní hodnoty a z nich určuje hodnotu celé formule.

Binárních booleovských spojek existuje 16: pro čtyři vstupy (0,0), (0,1), (1,0), (1,1) lze výstup 0/1 zvolit nezávisle, tedy 2⁴ způsoby.

## Poznámka Anki 1785298610670

Karty Anki: 1785298610670
GUID: OP`.ADZw@[; štítky: AI_combined::15_vyrokova_logika_SAT iterace_11 src_776-782.

### Otázka (Front)

Co jsou ohodnocení, model, splnitelnost, validita, kontradikce a SAT?

### Odpověď (Back)

**Ohodnocení** α:Var(φ)→{False,True}. Zápis α⊧φ znamená, že α formuli splňuje a je jejím **modelem**.
• φ je **splnitelná**, má-li alespoň jeden model.
• Je **validní/tautologie**, splňuje-li ji každé ohodnocení.
• Je **kontradikce/nesplnitelná**, nesplňuje-li ji žádné.

Platí: φ je validní ⇔ ¬φ je nesplnitelná; φ je nesplnitelná ⇔ ¬φ je validní. **SAT** rozhoduje, zda formule má alespoň jeden model; obecný SAT je NP-úplný.

## Poznámka Anki 1785298610671

Karty Anki: 1785298610671
GUID: gPV^f>IT{); štítky: AI_combined::15_vyrokova_logika_SAT iterace_11 src_783-790.

### Otázka (Front)

Co je CNF, proč se úlohy převádějí na SAT a jaké jsou hlavní typy SAT solverů?

### Odpověď (Back)

**Literál** je proměnná nebo její negace, **klauzule** disjunkce literálů a **term** konjunkce literálů. **CNF** je konjunkce klauzulí; podobně jako CSP každá klauzule omezuje povolená booleovská přiřazení a všechna omezení musí platit současně.

Převod na SAT/CSP umožní využít obecné solvery s propagací, heuristikami, učením a backjumpingem. Ve verifikaci model formule popisující nežádoucí běh dává protipříklad, nesplnitelnost jej v dané aproximaci vyloučí. V plánování model φ<sub>k</sub> odpovídá plánu pevné délky k.

**CDCL** kombinuje jednotkovou propagaci, heuristické větvení, backtracking/backjumping a učení konfliktních klauzulí. Systematické solvery mohou dokázat SAT i UNSAT; lokální GSAT/WalkSAT mění přiřazení a hledá model, ale obecně nedokazuje nesplnitelnost.

## Poznámka Anki 1785298610672

Karty Anki: 1785298610672
GUID: k7z,,/`Niw; štítky: AI_combined::15_vyrokova_logika_SAT iterace_11 src_791-795.

### Otázka (Front)

Jak funguje přímé (one-hot) zakódování konečnědoménové CSP proměnné do SAT?

### Odpověď (Back)

Pro každou hodnotu d∈D vznikne booleovská proměnná y<sub>d</sub> s významem x=d.
• **Alespoň jedna hodnota:** y₁∨…∨y<sub>|D|</sub>.
• **Nejvýše jedna:** pro každé d<e klauzule ¬y<sub>d</sub>∨¬y<sub>e</sub>.
Společně dávají právě jednu hodnotu.

Pro x₁=x₂ se pro každé d vynutí y<sub>d,1</sub>⇔y<sub>d,2</sub> (nebo disjunkce společně zvolených hodnot). Pro x₁≠x₂ se pro každé d přidá ¬y<sub>d,1</sub>∨¬y<sub>d,2</sub>, takže nemohou zvolit stejnou hodnotu.

## Poznámka Anki 1785298610673

Karty Anki: 1785298610673
GUID: z>].x*$.3:; štítky: AI_combined::15_vyrokova_logika_SAT iterace_11 src_796-804.

### Otázka (Front)

Jak funguje binární kódování CSP do SAT a jak se porovnává s one-hot kódováním?

### Odpověď (Back)

**Binární kódování** zapisuje hodnotu pomocí ⌈log₂|D|⌉ bitů; není-li |D| mocnina 2, musí zakázat neplatné bitové kombinace. Rovnost znamená ekvivalenci odpovídajících bitů; nerovnost, že se alespoň jeden bit liší, např. přes pomocné XOR proměnné a jejich disjunkci.

**One-hot:** |D| proměnných, větší formule, ale literály přímo značí hodnoty a jednotková propagace bývá silnější. **Binární:** jen ⌈log₂|D|⌉ proměnných, avšak doménové důsledky jsou rozptýlené přes bity a propagace může být slabší.

Volba kódování závisí také na počtu/délce klauzulí, pomocných proměnných, snadnosti omezení, hustotě modelů a symetriích. Symetrie nutí solver procházet strukturálně ekvivalentní, pouze přejmenované části prostoru.

