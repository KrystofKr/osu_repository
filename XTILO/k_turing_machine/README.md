# Obecný k-páskový Turingův stroj

Samostatná varianta projektu `XTILO/turing_machine`. Původní jednopáskové
moduly, testy a README zůstávají beze změny. Používá se pouze standardní
knihovna Pythonu 3.10+.

## Navržená struktura

```text
k_turing_machine/
├── __init__.py
├── __main__.py
├── state.py
├── tape.py
├── transition.py
├── machine.py
├── machines/
│   ├── __init__.py
│   ├── copy_machine.py
│   └── exercise_machine.py
├── tests/
│   ├── __init__.py
│   ├── test_machine.py
│   └── test_exercise_machine.py
└── README.md
```

## Návrh algoritmu cvičení před zápisem přechodů

Stroj používá přesně dvě pásky. `T1` je vstupní a výsledná páska, `T2` pracovní.
Vstupní abeceda je `Σ = {a, b, c, d, e}`. Celá pásková abeceda je
`Γ = {a, b, c, d, e, 0, 1, #}`. Pomocné značky využívají pouze její symboly;
žádné nové znaky se nepřidávají.

1. **Příprava:** na pozici `-1` pásky `T1` zapiš značku `0`, aby šlo později
   najít začátek i po vymazání vstupu.
2. **Filtrování:** projdi původní vstup zleva doprava. Stavy liché a sudé
   pozice se střídají po každém původním symbolu. Uchovávané symboly přenes
   souvisle na `T2`; `a/e` na sudé pozici přeskoč. Původní buňky na `T1`
   přitom maž. Při smazání se parita následující původní pozice také změní.
3. **Návrat:** označ pravý konec pracovní oblasti `T2` symbolem `0` a její
   levý okraj na pozici `-1` symbolem `1`. Na `T1` najdi přípravnou značku,
   smaž ji a vrať se na pozici `0`.
4. **Řazení:** projdi celou pracovní oblast `T2` pětkrát, postupně pro
   `a`, `b`, `c`, `d`, `e`. Během každého průchodu přenášej hledané písmeno
   na konec výsledku na `T1` a maž je z `T2`. Ostatní symboly i vzniklé
   blankové mezery přeskoč. Okrajové značky umožňují projít i přes tyto mezery.
   Výsledek na `T1` je souvislý a vzestupně setříděný.
5. **Příprava čítače:** vymaž pracovní oblast i obě značky na `T2`.
   Zapiš tam pomocnou levou značku `a` na pozici `-1` a binární nulu na pozici
   `0`. Binární čítač bude ukládat nejméně významný bit vlevo.
6. **Počítání:** projdi setříděné slovo na `T1` zprava doleva. Za každé
   písmeno přičti na `T2` jednu přechody s přenosem: `1` změň na `0` a
   pokračuj doprava, první `0` nebo blank změň na `1`. Potom se vrať po bitech
   k levé značce čítače a přesuň hlavu `T1` na další písmeno vlevo.
7. **Zápis délky:** na `T1` najdi konec setříděného slova a ponech za ním
   právě jeden blank. Najdi pravý konec čítače na `T2` a kopíruj bity zprava
   doleva na `T1` směrem doprava. Tím vznikne běžný binární zápis od nejvíce
   významného bitu. Kopírované bity na `T2` současně maž.
8. **Úklid a halt:** smaž levou značku čítače na `T2` a přejdi do koncového
   stavu. `T2` je prázdná. Pro prázdný výsledný řetězec zůstane na `T1` `#0`.

Celá realizace je tvořena přechody. Python smí sestavit pevnou přechodovou
tabulku a ověřit vstupní abecedu, nikoli filtrovat, třídit či měřit slovo.

## Rozpor v ukázkovém výsledku zadání

V zadání je uveden vstup `aaebcceaabecddaecbaedeeee` a výsledek
`aaaaabbbccccdddeeeee#10011`. Uvedené setříděné slovo má 20 písmen, ale
binární délka `10011` znamená 19. Podle pravidla mazání na pozicích
`2, 4, 6, ...` vychází `aaaabbbccccdddeeeee#10011` (čtyři `a`, celkem 19).
Při číslování od nuly by vyšlo `aabbbccccdddeeee#10000`.
Uživatel potvrdil číslování od jedné a mazání na pozicích `2, 4, ...`.
Povinný test proto ověřuje `aaaabbbccccdddeeeee#10011`. Ukázka ze zadání
obsahuje jedno nadbytečné `a`; stroj se řídí potvrzeným pravidlem.

## Co se změnilo oproti jednopáskové verzi

`state.py` a základ pásky byly zkopírovány do nového balíčku. Nová `Machine`
přijímá počet pásek `k` a neměnnou n-tici samostatných objektů `Tape`.
Každá páska má vlastní slovník, hlavu a interval navštívených buněk.
Počet pásek i šířka každého přechodu se při vytváření stroje kontrolují.
Stejný objekt `Tape` nelze použít pro dvě různé pásky.

Přechod obsahuje n-tice místo jednotlivých symbolů a pohybu. Slovník přechodů
je indexován dvojicí `(State, tuple[str, ...])`. `RunResult` obsahuje společný
stav a počet kroků, samostatný `TapeResult` pro každou pásku a celkový počet
navštívených buněk. Logika konkrétní úlohy je pouze v `machines/`.

Nová metoda `Tape.content()` zahrnuje do relevantního úseku také pozici `0`,
aby například prázdný výsledný řetězec zachoval svůj oddělovač v zápisu `#0`.
Páska bez neblankových buněk vrací `""`, což označuje vyčištěnou `T2`.
Vnitřní blanky zůstávají součástí obsahu.

## Stav, páska a přechod

`State("q0")` je neměnný datový objekt s atributem `id`. Stejné identifikátory
označují stejné stavy. `Tape.cells` je `dict[int, str]`, neuložená buňka
obsahuje blank `#`. Zápis blanku odstraní buňku ze slovníku. Hlavy začínají
na pozici `0`; záporné pozice mají stejný význam jako kladné.

Přechod pro dvě pásky:

```python
from k_turing_machine import State, Transition

transition = Transition(
    state=State("q0"),
    read_symbols=("a", "#"),
    next_state=State("q1"),
    write_symbols=("#", "a"),
    operations=("R", "L"),
)
```

Tento přechod přečte `a` z `T1` a blank z `T2`, vymaže původní `a`,
zapíše `a` na `T2` a přejde do `q1`. Hlava `T1` se posune doprava,
hlava `T2` doleva. `S` ponechá hlavu na místě. Všechny symboly musí
být jednoznakové; n-tice čtení, zápisů a pohybů mají stejnou nenulovou délku.
Pro determinismus je pro každý klíč povolen nejvýše jeden přechod.

## Co provede jeden `step()`

1. V koncovém stavu vrátí `False` a nic nemění.
2. Přečte **všechny** pásky ještě před jakýmkoli zápisem:
   `read_symbols = tuple(tape.read() for tape in self.tapes)`.
3. Vyhledá přechod pro `(self.state, read_symbols)`.
4. Zapíše nové symboly do původních pozic všech hlav.
5. Posune každou hlavu podle její vlastní operace.
6. Změní společný stav a zvýší `step_count` o **jednu**, nezávisle na `k`.

Hlavní část provádění:

```python
def execute_transition(self, transition: Transition) -> None:
    for tape, symbol in zip(self.tapes, transition.write_symbols):
        tape.write(symbol)
    for tape, direction in zip(self.tapes, transition.operations):
        tape.move(direction)
    self.state = transition.next_state
    self.step_count += 1
```

Chybějící přechod mimo koncový stav vyvolá `MissingTransitionError`
s názvem stavu, čtenou n-ticí a polohami hlav. Pásky a čítač se přitom nezmění.

## `run()`, limit a trasování

`run(max_steps=100_000, trace=False)` opakuje `step()` do koncového stavu.
Limit se týká nových přechodů v tomto konkrétním volání. Při jeho vyčerpání
vyvolá `StepLimitExceeded`; ve stejném stroji lze pokračovat dalším `run()`.
Celkový čítač ani statistiky návštěv se při pokračování nenulují.
Dokončení na posledním povoleném kroku je úspěch. Nulový limit lze použít
pro návrat výsledku již zastaveného stroje.

`trace=True` po každém přechodu vypíše společný stav, číslo kroku a každou
pásku s označením `T1`, `T2`, ... a ukazatelem hlavy `^`. Poloha `head`
je absolutní index. Údaje `read`, `write`, `move` popisují právě provedený
přechod: `read` zde označuje symboly **před** zápisem a pohybem.

Po prvním kroku kopírovacího stroje se vstupem `abc`:

```text
step: 1
state: qCopy
read:  ('a', '#')
write: ('a', 'a')
move:  ('R', 'R')

T1: ##abc##
       ^
head: 1

T2: ##a###
       ^
head: 1
```

## Jak definovat vlastní stroj

Vytvořte stavy, přechody a počáteční pásky. Simulátor se nemění.
Úplný dvoupáskový příklad kopírující pouze `a`:

```python
from k_turing_machine import Machine, State, Tape, Transition

q0, halt = State("q0"), State("halt")
transitions = [
    Transition(q0, ("a", "#"), q0, ("a", "a"), ("R", "R")),
    Transition(q0, ("#", "#"), halt, ("#", "#"), ("S", "S")),
]
machine = Machine(
    k=2,
    states={q0, halt},
    transitions=transitions,
    initial_state=q0,
    halt_states={halt},
    tapes=(Tape("aaa"), Tape()),
)
result = machine.run()
print(result.tapes[1].tape_content)  # aaa
```

Pro tři pásky se použije `k=3`, tři objekty `Tape` a trojice ve všech
přechodech. Následující jednorázový přechod demonstruje tři různé pohyby:

```python
from k_turing_machine import Machine, State, Tape, Transition

q0, halt = State("q0"), State("halt")
machine = Machine(
    k=3,
    states={q0, halt},
    transitions=[
        Transition(q0, ("a", "#", "#"), halt, ("a", "b", "c"), ("R", "L", "S")),
    ],
    initial_state=q0,
    halt_states={halt},
    tapes=(Tape("a"), Tape(), Tape()),
)
print(tuple(tape.head for tape in machine.run().tapes))  # (1, -1, 0)
```

Podporováno je libovolné kladné `k`, včetně `1`. Množina koncových stavů
může být prázdná; pak běh skončí až chybou nebo vyčerpáním limitu.

## Přechodová tabulka cvičení

`machines/exercise_machine.py` definuje 25 stavů a 154 přechodů.
Funkce `_build_definition()` používá smyčky nad **pevnou** abecedou a
pravidly k rozepsání přechodové tabulky. Nemá parametr vstupu a nečte pásky.
Například smyčka pro pět třídicích průchodů pouze vytváří stavy
`qSelect_a` až `qSelect_e` a jejich přechody.

`make_exercise_machine()` ověří abecedu a vloží původní vstup beze změny
na `T1`. Nefiltruje, netřídí a nepočítá jeho délku. Při běhu se vykonávají
jen přechody obecného simulátoru.

| Stavy | Význam |
| --- | --- |
| `qStart`, `qMarkLeft` | příprava levé značky na T1 |
| `qFilterOdd`, `qFilterEven` | filtrace podle původní pozice |
| `qRewindT1`, `qRewindT2` | návrat hlav a ohraničení T2 |
| `qSelect_a` až `qSelect_e`, `qRewind_a` až `qRewind_d` | řazení pevnými průchody |
| `qClearT2`, `qInitCounterMarker`, `qInitCounterZero` | úklid pracovní oblasti a příprava čítače |
| `qCount`, `qCarry`, `qCounterReturn` | binární inkrementace za každé písmeno |
| `qSeekOutputEnd`, `qSeekCounterEnd`, `qCopyBits` | oddělovač a zápis binární délky |
| `qHalt` | vyčištěná T2, dokončený výsledek na T1 |

Třídicí průchody jsou ve vzestupném pořadí písmen. Každý přenesený symbol
posune hlavu `T1` doprava, jiné symboly ji neposouvají. Výsledné slovo je
proto souvislé. Okraje `T2` jsou při třídění `1` a `0`; při počítání se
znovu používá již vyčištěná páska, kde značkou levého okraje je `a`.

## Měření kroků a použitých buněk

`step_count` počítá úspěšně provedené přechody, včetně přechodu do koncového
stavu a přechodů s `S`. Jeden společný přechod je jeden krok bez ohledu
na počet pásek. Tisk trasování nepřidává kroky simulovaného stroje.

Za **použitou buňku** se počítá každá různá pozice, kterou navštívila hlava
dané pásky, včetně blanků, pomocných značek a počáteční pozice `0`.
Započítá se i buňka dosažená posledním pohybem, přestože v ní už nedojde
ke čtení. Opakované návštěvy počet nezvyšují. Předběžné uložení celého
vstupu do slovníku samo o sobě není návštěva hlavy.

Pohyb o jednu buňku vytváří souvislý interval navštívených pozic, proto:

```python
visited_cells = rightmost_visited - leftmost_visited + 1
total_used_cells = sum(tape.visited_cells for tape in result.tapes)
```

To je metrika prostoru využitého během celého běhu. `len(tape.cells)`
by naopak měřilo jen právě uložené neblankové buňky, takže by po vyčištění
pracovní pásky ztratilo informaci o jejím použití.

## Spuštění a naměřený povinný výsledek

Příkazy se spouštějí z adresáře `XTILO`, stejně jako původní projekt:

```bash
cd /home/grogy/osu_repository/XTILO

# Základní kopírovací stroj a jeho trasování.
python3 -m k_turing_machine copy abc
python3 -m k_turing_machine copy abc --trace

# Bez explicitního vstupu použije exercise povinný vstup ze zadání.
python3 -m k_turing_machine exercise
python3 -m k_turing_machine exercise 'aaebcceaabecddaecbaedeeee'
python3 -m k_turing_machine exercise 'baea' --trace --max-steps 1000
python3 -m k_turing_machine exercise ''

# Nové testy / všechny nové i původní testy.
python3 -m unittest discover -s k_turing_machine/tests -t . -v
python3 -m unittest discover -v
```

Výstup skutečně provedeného běhu povinného vstupu:

```text
Konečný stav: qHalt
steps = 379
T1 content = 'aaaabbbccccdddeeeee#10011'
T1 head = 25
T1 visited range = [-1, 25]
T1 used cells = 27
T2 content = ''
T2 head = 0
T2 visited range = [-1, 19]
T2 used cells = 21
total used cells = 48
```

`T2 content = ''` znamená, že `T2.cells` je prázdný slovník a všechny její
buňky obsahují `#`. Počet 379 přechodů i prostorové statistiky naměřil
simulátor; nejsou odvozeny náhradním algoritmem nad vstupním řetězcem.
Po potvrzené opravě ukázky odpovídá výsledek pravidlu mazání i binární délce.

Obecně při vstupu délky `n` zabírá stroj lineární prostor. Filtrace,
návraty a pět třídicích průchodů mají lineární počet kroků. Binární
inkrementace prochází jen bity zasažené přenosem a vrací se přes ně;
přenosy se přes všechny inkrementace amortizují na lineární čas.
Pro pevnou pětipísmennou abecedu má proto tento konkrétní algoritmus
časovou i prostorovou složitost `Θ(n + 1)`. Naměřený jednotlivý běh
sám o sobě tento asymptotický odhad nedokazuje.

## Testy

Nová varianta má 24 unit testů: 15 testů infrastruktury a 9 testů cvičení
s více ručně zadanými případy. Ověřují dvě i tři pásky, `R/L/S`, negativní
pozice, chybějící a duplicitní přechody, nekonečný běh a jeho limit,
pokračování běhu, trasování i statistiky.

Testy cvičení kontrolují skutečné slovníky buněk obou pásek, prázdný vstup,
paritu původních pozic, řazení s chybějícími skupinami písmen, binární
přenosy přes více bitů a růst výstupu přes pravý okraj původního vstupu.
Kontrolují také mezifáze a povolenou abecedu během každého kroku povinného
vstupu. Očekávané výsledky jsou zadány ručně; testy nemají alternativní
implementaci filtrace, třídění ani výpočtu binární délky.

Společný běh s původními jednopáskovými testy dokončil všech 48 testů.
