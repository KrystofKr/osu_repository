# Obecný simulátor Turingova stroje

Studijní implementace deterministického jednopáskového Turingova stroje v Pythonu.
Používá pouze standardní knihovnu, type hints a pásku neomezenou v obou směrech.
Vyžaduje Python 3.10 nebo novější; ověřeno na Pythonu 3.12.3.

## Soubory a architektura

```text
XTILO/
├── .gitignore
├── README.md
└── turing_machine/
    ├── __init__.py       # veřejné třídy simulátoru
    ├── __main__.py       # příkazová řádka
    ├── state.py          # State: identifikátor stavu
    ├── transition.py     # Transition: jeden přechod
    ├── tape.py           # Tape: buňky, hlava, statistiky a výpis
    ├── machine.py        # Machine: obecné provádění přechodů
    ├── examples.py       # tabulky skeneru a binárního porovnání
    └── test_machine.py   # unit testy
```

`Machine` provádí přechody, `Tape` uchovává symboly a polohu hlavy.
Konkrétní algoritmus určují data v `examples.py`. Změna stroje nevyžaduje
změnu metod `step()` ani `run()`.

## Spuštění

Všechny následující příkazy spusťte z adresáře `XTILO`:

```bash
cd /home/grogy/osu_repository/XTILO

# Jednoduchý stroj projede slovo a zastaví se na prvním blanku.
python3 -m turing_machine scan 1010
python3 -m turing_machine scan 1010 --trace

# Porovnání x>y. Uvozovky chrání znak > před přesměrováním v shellu.
python3 -m turing_machine compare '100>10'
python3 -m turing_machine compare '10>10'
python3 -m turing_machine compare '1>10'
python3 -m turing_machine compare '100>10' --trace --max-steps 1000

# Všechny unit testy.
python3 -m unittest discover -v
```

Předepsané příklady:

| Vstup | Výsledný obsah pásky | Počet kroků | Navštívené buňky |
| --- | --- | ---: | ---: |
| `100>10` | `1` | 43 | 8 |
| `10>10` | `0` | 37 | 7 |
| `1>10` | `0` | 21 | 6 |

Například první příkaz pro porovnání vypíše:

```text
Konečný stav: qHalt
Počet kroků: 43
Obsah pásky: '1'
Nejlevější navštívená buňka: -1
Nejpravější navštívená buňka: 6
Počet navštívených buněk: 8
```

## 1. Reprezentace pásky

`Tape.cells` je slovník `dict[int, str]`. Vstup `100>10` se uloží jako:

```python
{0: "1", 1: "0", 2: "0", 3: ">", 4: "1", 5: "0"}
```

Hlava začíná na pozici `0`. `read()` čte aktuální buňku pomocí
`cells.get(head, blank_symbol)`. Chybějící pozice obsahuje blank `#`.
Zápis blanku odstraní buňku ze slovníku; jiné symboly ji vytvoří nebo přepíší.
Páska se tedy nemusí fyzicky rozšiřovat o prázdné buňky.

`move("L")` odečte od pozice hlavy jednu, `move("R")` přičte jednu a
`move("S")` hlavu ponechá na místě. Záporné indexy mají stejný význam jako
kladné. Pro správné sledování návštěv přesouvejte hlavu metodou `move()`.
Vlastní blank lze nastavit například pomocí `Tape("aba", blank_symbol="_")`.

`content()` vrátí úsek od nejlevější do nejpravější neblankové buňky,
včetně případných blanků uvnitř. U úplně prázdné pásky vrátí prázdný řetězec.
`render()` zobrazí i aktuální hlavu, dva okrajové blanky a ukazatel `^`.

## 2. Reprezentace stavu

Stav je neměnný datový objekt `State` s identifikátorem `id`:

```python
from turing_machine import State

q0 = State("q0")
halt = State("halt")
```

Dva objekty `State` se stejným `id` označují tentýž stav. Neměnnost umožňuje
jejich použití v množinách a jako části klíče slovníku přechodů.

## 3. Reprezentace přechodu

Přechod `δ(q0, 1) = (q1, 0, R)` se zapíše datově:

```python
from turing_machine import State, Transition

transition = Transition(
    state=State("q0"),
    read_symbol="1",
    next_state=State("q1"),
    write_symbol="0",
    operation="R",
)
```

Povolené operace jsou `L`, `R` a `S`. Každý symbol má právě jeden znak.
Konstruktor `Machine` indexuje přechody slovníkem
`(stav, čtený_symbol) -> Transition`, takže hledání má běžně konstantní čas.
Více přechodů se stejným klíčem odmítne, protože stroj musí být deterministický.
Také ověřuje, že počáteční stav, koncové stavy a stavy přechodů jsou definované.
Množina koncových stavů může být prázdná; takový běh zastaví až limit kroků
nebo chyba chybějícího přechodu.
Abecedu konkrétního stroje určují jeho vstup a přechody; obecný simulátor ji
neomezuje na binární symboly.

## 4. Jeden krok `step()`

`step()` provede přesně jeden přechod:

1. Pokud je aktuální stav koncový, vrátí `False` beze změny konfigurace.
2. `find_transition()` přečte symbol pod hlavou a najde dvojici `(state, symbol)`.
3. `execute_transition()` zapíše nový symbol do původní buňky.
4. Změní aktuální stav na `next_state`.
5. Posune hlavu podle operace `L/R/S`.
6. Zvýší `step_count` o jednu a `step()` vrátí `True`.

Hlavní část provádění v `machine.py`:

```python
def execute_transition(self, transition: Transition) -> None:
    self.tape.write(transition.write_symbol)
    self.state = transition.next_state
    self.tape.move(transition.operation)
    self.step_count += 1

def step(self) -> bool:
    if self.halted:
        return False
    transition = self.find_transition()
    self.execute_transition(transition)
    return True
```

Pokud přechod chybí mimo koncový stav, vznikne `MissingTransitionError`
s názvem stavu, čteným symbolem a pozicí hlavy. Chybějící přechod se nepočítá
jako krok a nemění pásku.

## 5. Běh `run()` a trasování

`run()` opakuje `step()`, dokud stroj nevstoupí do koncového stavu.
Potom vrátí `RunResult` se statistikami. Jeho smyčka neobsahuje logiku
skeneru ani porovnání čísel.

```python
from turing_machine.examples import make_comparator

machine = make_comparator("100>10")
result = machine.run(max_steps=1000, trace=True)
print(result.tape_content)  # 1
```

`max_steps` omezuje počet **nových přechodů v jednom volání**; výchozí limit
je `100_000`. Po vyčerpání vznikne `StepLimitExceeded` a konfigurace zůstane
dostupná. Lze pokračovat dalším `run()` s novým limitem. Celkový `step_count`
se při pokračování nenuluje. Zastavení přesně na posledním povoleném kroku
je úspěšné. Limit `0` dovoluje jen návrat výsledku již zastaveného stroje.

Volba `trace=True` vypisuje konfiguraci **po každém provedeném přechodu**.
`read` proto označuje symbol pod hlavou po jejím posunutí, nikoli původně
čtený symbol. Například po prvním kroku skeneru nad `1010`:

```text
step: 1
state: qScan
head: 1
read: 0
tape:
##1010##
   ^
```

## 6. Jak definovat vlastní stroj

Definujte množinu stavů, seznam přechodů, počáteční stav, množinu koncových
stavů a vstupní pásku. Tento úplný příklad obrátí bity vstupního slova:

```python
from turing_machine import Machine, State, Tape, Transition

q0, halt = State("q0"), State("halt")
transitions = [
    Transition(q0, "0", q0, "1", "R"),
    Transition(q0, "1", q0, "0", "R"),
    Transition(q0, "#", halt, "#", "S"),
]
machine = Machine(
    states={q0, halt},
    transitions=transitions,
    initial_state=q0,
    halt_states={halt},
    tape=Tape("1010"),
)
print(machine.run().tape_content)  # 0101
```

Do `examples.py` lze přidat obdobnou definici. Pro cvičení s porovnáním
slouží jako výchozí kostra konstanty `COMPARISON_INPUT_ALPHABET`,
`COMPARISON_TAPE_ALPHABET`, `COMPARISON_STATES` a `COMPARISON_RULES`.
Poslední konstanta obsahuje čitelnou tabulku pětic
`(stav, čtení, nový_stav, zápis, pohyb)`, která se převádí na objekty `Transition`.
Úpravou stavů a této tabulky lze měnit algoritmus bez zásahu do simulátoru.

## Stroj pro `x>y`

Vstupní abeceda je `Σ = {0, 1, >}` a pásková abeceda `Γ = {0, 1, >, #}`.
Vstup má tvar `x>y`, kde obě strany obsahují alespoň jednu binární číslici.
Kladná čísla ze zadání jsou podporována; fungují také nuly a úvodní nuly.
Přípravná funkce ověřuje pouze formát, bez převodu na čísla. Porovnání,
dekrementaci a úklid pásky provádějí výhradně přechody.

Algoritmus:

1. Projdi `x`. Pokud neobsahuje žádnou jedničku, skonči s výsledkem `0`.
2. Projdi `y`. Pokud neobsahuje žádnou jedničku, skonči s výsledkem `1`.
3. Obě čísla jsou kladná. Odečti od `y` jedničku a potom ji odečti od `x`.
4. Vrať se na začátek a opakuj. Odečítání stejné hodnoty zachovává vztah čísel.
5. Před zastavením smaž celý původní vstup a zapiš jediný výsledek na pozici `0`.

Binární dekrementace probíhá zprava doleva: koncové `0` mění na `1` a postupuje
doleva, první `1` změní na `0` a ukončí půjčování. Například `100` se změní na
`011`. Počet číslic zůstává stejný, což umožňuje používat pouze zadanou abecedu.
Kontrola kladnosti před dekrementací brání půjčování přes levý okraj čísla.

| Stavy | Úloha |
| --- | --- |
| `qCheckX`, `qXPositive` | zjistit, zda je `x` kladné, a dojít k oddělovači |
| `qCheckY`, `qSeekEndY` | zjistit, zda je `y` kladné, a dojít na jeho konec |
| `qDecY`, `qBackToSeparator` | snížit `y` o jedna a vrátit se k `>` |
| `qDecX`, `qReturnStart` | snížit `x` o jedna a vrátit se na začátek |
| `qSeekEnd0` | najít pravý okraj vstupu před zápisem výsledku `0` |
| `qEraseLeft0`, `qEraseLeft1` | vymazat celý vstup zprava doleva |
| `qWrite0`, `qWrite1` | zapsat výsledek na pozici `0` |
| `qHalt` | zastavit |

Pro `100>10` projde stroj postupně číselnými konfiguracemi
`100>10`, `011>01`, `010>00`. Pak zjistí kladné `x` a nulové `y`, vymaže vstup
a zanechá `1`. Pro stejná čísla dosáhnou obě nuly současně; první kontrola
`x` rozhodne o výsledku `0`.

## 7. Počet kroků a časová složitost

`step_count` začíná na nule. Každý provedený přechod přičte jednu, včetně
přechodu do koncového stavu a operace `S`. Čtení, tisk a neúspěšné hledání
přechodu další kroky nepřidávají. Čítač měří kroky simulovaného stroje,
nikoli počet instrukcí Pythonu ani čas trasování.

Skener nad slovem délky `n` provede přesně `n + 1` kroků: `n` posunů a
jeden přechod do koncového stavu na blanku.

U porovnání označme `n` délku celého vstupu včetně `>` a `k = min(x, y)`
číselnou hodnotu menšího operandu. Stroj provede `k` úplných dekrementací.
Každá trvá `2(n + 1)` kroků a závěrečná kontrola s úklidem `2n + 3` kroků.
Celkem tedy provede `2(n + 1)(k + 1) + 1` kroků; časová složitost je
`Θ(n(k + 1))`.

Tento snadno sledovatelný algoritmus může být exponenciálně pomalý vzhledem
k počtu binárních číslic. U velkých hodnot je proto vhodné hlídat `max_steps`.
Tabulku lze později nahradit jiným algoritmem a statistiky použít ke srovnání.

## 8. Navštívené buňky a prostorová složitost

Páska sleduje nejlevější a nejpravější navštívenou pozici. Za navštívenou
se od začátku počítá buňka `0` a dále každá pozice, na kterou hlava dorazí,
včetně blanků. Návrat na již navštívenou buňku počet nezvýší.

Hlava se pohybuje po jedné buňce, takže navštívené pozice tvoří souvislý interval:

```python
visited_cells = rightmost_visited - leftmost_visited + 1
```

`len(tape.cells)` udává počet právě uložených neblankových buněk, což je jiná
veličina. Po dokončení porovnání je uložena jen jedna buňka s výsledkem,
ale počet navštívených buněk zachovává prostor použitý při celém výpočtu.
Samotné vložení vstupu do slovníku se nepočítá jako návštěva hlavy.

Skener navštíví pozice `0` až `n`, tedy `n + 1` buněk. Porovnávací stroj
navštíví pozice `-1` až `n`, tedy `n + 2` buněk, nezávisle na počtu
dekrementací. Prostorová složitost je v obou případech `Θ(n)`.

Výsledek je dostupný také programově:

```python
from turing_machine.examples import make_comparator

result = make_comparator("100>10").run()
print(result.final_state)
print(result.step_count)
print(result.tape_content)
print(result.leftmost_visited, result.rightmost_visited, result.visited_cells)
```

Testy ověřují pásku, pohyb oběma směry, přechody, determinismus, chybové stavy,
limit a pokračování běhu, trasování i výsledky porovnání. Obsahují také všech
256 dvojic hodnot `0–15`, každou ve čtyřech variantách úvodních nul
(celkem 1024 porovnávacích běhů). Běžné Pythonové porovnání se používá pouze
v testech jako nezávislá kontrola očekávaného výsledku.
