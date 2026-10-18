"""Definice ukázkových strojů. Jejich algoritmy jsou v přechodových tabulkách."""

from .machine import Machine
from .state import State
from .tape import Tape
from .transition import Direction, Transition


SCAN_STATES = {name: State(name) for name in ("qScan", "qHalt")}
SCAN_TRANSITIONS = (
    Transition(SCAN_STATES["qScan"], "0", SCAN_STATES["qScan"], "0", "R"),
    Transition(SCAN_STATES["qScan"], "1", SCAN_STATES["qScan"], "1", "R"),
    Transition(SCAN_STATES["qScan"], "#", SCAN_STATES["qHalt"], "#", "S"),
)


def make_scanner(input_word: str) -> Machine:
    """Projede binární slovo doprava a zastaví se na prvním blanku."""
    if any(symbol not in "01" for symbol in input_word):
        raise ValueError("Vstup skeneru smí obsahovat pouze 0 a 1.")
    return Machine(
        states=SCAN_STATES.values(),
        transitions=SCAN_TRANSITIONS,
        initial_state=SCAN_STATES["qScan"],
        halt_states={SCAN_STATES["qHalt"]},
        tape=Tape(input_word),
    )


COMPARISON_INPUT_ALPHABET = frozenset({"0", "1", ">"})
COMPARISON_TAPE_ALPHABET = COMPARISON_INPUT_ALPHABET | {"#"}
COMPARISON_STATES = {
    name: State(name)
    for name in (
        "qCheckX", "qXPositive", "qCheckY", "qSeekEndY", "qDecY",
        "qBackToSeparator", "qDecX", "qReturnStart", "qSeekEnd0",
        "qEraseLeft0", "qEraseLeft1", "qWrite0", "qWrite1", "qHalt",
    )
}

# Každý řádek obsahuje (stav, čtení, nový stav, zápis, pohyb).
# Šířky čísel se při dekrementaci zachovávají, včetně úvodních nul.
COMPARISON_RULES: tuple[tuple[str, str, str, str, Direction], ...] = (
    # Zjisti, zda je x nula. Pokud ano, výsledek je 0.
    ("qCheckX", "0", "qCheckX", "0", "R"),
    ("qCheckX", "1", "qXPositive", "1", "R"),
    ("qCheckX", ">", "qSeekEnd0", ">", "R"),
    ("qXPositive", "0", "qXPositive", "0", "R"),
    ("qXPositive", "1", "qXPositive", "1", "R"),
    ("qXPositive", ">", "qCheckY", ">", "R"),

    # x je kladné. Nulové y znamená výsledek 1.
    ("qCheckY", "0", "qCheckY", "0", "R"),
    ("qCheckY", "1", "qSeekEndY", "1", "R"),
    ("qCheckY", "#", "qEraseLeft1", "#", "L"),

    # Najdi konec y a odečti jedničku binárním půjčováním.
    ("qSeekEndY", "0", "qSeekEndY", "0", "R"),
    ("qSeekEndY", "1", "qSeekEndY", "1", "R"),
    ("qSeekEndY", "#", "qDecY", "#", "L"),
    ("qDecY", "0", "qDecY", "1", "L"),
    ("qDecY", "1", "qBackToSeparator", "0", "L"),

    # Od oddělovače odečti jedničku také od x.
    ("qBackToSeparator", "0", "qBackToSeparator", "0", "L"),
    ("qBackToSeparator", "1", "qBackToSeparator", "1", "L"),
    ("qBackToSeparator", ">", "qDecX", ">", "L"),
    ("qDecX", "0", "qDecX", "1", "L"),
    ("qDecX", "1", "qReturnStart", "0", "L"),

    # Vrať se na začátek a opakuj kontrolu obou čísel.
    ("qReturnStart", "0", "qReturnStart", "0", "L"),
    ("qReturnStart", "1", "qReturnStart", "1", "L"),
    ("qReturnStart", "#", "qCheckX", "#", "R"),

    # Před úklidem výsledku 0 dojdi na pravý okraj vstupu.
    ("qSeekEnd0", "0", "qSeekEnd0", "0", "R"),
    ("qSeekEnd0", "1", "qSeekEnd0", "1", "R"),
    ("qSeekEnd0", "#", "qEraseLeft0", "#", "L"),

    # Smaž vstup zprava doleva, pak zapiš výsledek na pozici 0.
    ("qEraseLeft0", "0", "qEraseLeft0", "#", "L"),
    ("qEraseLeft0", "1", "qEraseLeft0", "#", "L"),
    ("qEraseLeft0", ">", "qEraseLeft0", "#", "L"),
    ("qEraseLeft0", "#", "qWrite0", "#", "R"),
    ("qWrite0", "#", "qHalt", "0", "S"),
    ("qEraseLeft1", "0", "qEraseLeft1", "#", "L"),
    ("qEraseLeft1", "1", "qEraseLeft1", "#", "L"),
    ("qEraseLeft1", ">", "qEraseLeft1", "#", "L"),
    ("qEraseLeft1", "#", "qWrite1", "#", "R"),
    ("qWrite1", "#", "qHalt", "1", "S"),
)
COMPARISON_TRANSITIONS = tuple(
    Transition(
        COMPARISON_STATES[state], read,
        COMPARISON_STATES[next_state], write, operation,
    )
    for state, read, next_state, write, operation in COMPARISON_RULES
)


def make_comparator(input_word: str) -> Machine:
    """Připraví porovnání x>y; Python ověřuje pouze tvar vstupu."""
    left, separator, right = input_word.partition(">")
    if not separator or not left or not right or any(
        symbol not in "01" for symbol in left + right
    ):
        raise ValueError("Vstup musí mít tvar x>y, kde x a y jsou neprázdná binární slova.")
    return Machine(
        states=COMPARISON_STATES.values(),
        transitions=COMPARISON_TRANSITIONS,
        initial_state=COMPARISON_STATES["qCheckX"],
        halt_states={COMPARISON_STATES["qHalt"]},
        tape=Tape(input_word),
    )
