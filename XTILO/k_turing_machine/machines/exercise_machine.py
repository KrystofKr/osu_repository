"""Filtrace původních pozic, řazení a binární délka výhradně přechody TS."""

from .. import Direction, Machine, State, Tape, Transition


LETTERS = ("a", "b", "c", "d", "e")
INPUT_ALPHABET = frozenset(LETTERS)
TAPE_ALPHABET = INPUT_ALPHABET | {"0", "1", "#"}
REQUIRED_INPUT = "aaebcceaabecddaecbaedeeee"


def _build_definition() -> tuple[frozenset[State], tuple[Transition, ...]]:
    """Rozepíše pevná pravidla tabulky; vstupní slovo tato funkce nezná."""
    states: set[State] = set()
    transitions: list[Transition] = []

    def add(
        state: str,
        read: tuple[str, str],
        next_state: str,
        write: tuple[str, str],
        move: tuple[Direction, Direction],
    ) -> None:
        source, target = State(state), State(next_state)
        states.update((source, target))
        transitions.append(Transition(source, read, target, write, move))

    # 1. Levá značka T1 je potřebná pro návrat po vymazání původního vstupu.
    for symbol in LETTERS + ("#",):
        add("qStart", (symbol, "#"), "qMarkLeft", (symbol, "#"), ("L", "S"))
    add("qMarkLeft", ("#", "#"), "qFilterOdd", ("0", "#"), ("R", "S"))

    # 2. Paritu měníme po každém původním znaku, i po smazaném a/e.
    for current, following in (("qFilterOdd", "qFilterEven"), ("qFilterEven", "qFilterOdd")):
        for symbol in LETTERS:
            if current == "qFilterEven" and symbol in ("a", "e"):
                add(current, (symbol, "#"), following, ("#", "#"), ("R", "S"))
            else:
                add(current, (symbol, "#"), following, ("#", symbol), ("R", "R"))
        add(current, ("#", "#"), "qRewindT1", ("#", "0"), ("L", "S"))

    # 3. Návrat T1 k pozici 0; ohraničení kompaktního slova na T2.
    add("qRewindT1", ("#", "0"), "qRewindT1", ("#", "0"), ("L", "S"))
    add("qRewindT1", ("0", "0"), "qRewindT2", ("#", "0"), ("R", "L"))
    for symbol in LETTERS:
        add("qRewindT2", ("#", symbol), "qRewindT2", ("#", symbol), ("S", "L"))
    add("qRewindT2", ("#", "#"), "qSelect_a", ("#", "1"), ("S", "R"))

    # 4. Pět pevných průchodů T2. Značky dovolují přecházet vymazané mezery.
    for target in LETTERS:
        scan, rewind = f"qSelect_{target}", f"qRewind_{target}"
        for symbol in LETTERS + ("#",):
            if symbol == target:
                add(scan, ("#", symbol), scan, (symbol, "#"), ("R", "R"))
            else:
                add(scan, ("#", symbol), scan, ("#", symbol), ("S", "R"))
        if target == "e":
            add(scan, ("#", "0"), "qClearT2", ("#", "#"), ("S", "L"))
        else:
            add(scan, ("#", "0"), rewind, ("#", "0"), ("S", "L"))
            for symbol in LETTERS + ("#",):
                add(rewind, ("#", symbol), rewind, ("#", symbol), ("S", "L"))
    for current, following in (("a", "b"), ("b", "c"), ("c", "d"), ("d", "e")):
        add(f"qRewind_{current}", ("#", "1"), f"qSelect_{following}",
            ("#", "1"), ("S", "R"))

    # 5. T2 je nyní mezi značkami prázdná. Připrav čítač a levou značku a.
    add("qClearT2", ("#", "#"), "qClearT2", ("#", "#"), ("S", "L"))
    add("qClearT2", ("#", "1"), "qInitCounterMarker", ("#", "#"), ("S", "S"))
    add("qInitCounterMarker", ("#", "#"), "qInitCounterZero", ("#", "a"), ("S", "R"))
    add("qInitCounterZero", ("#", "#"), "qCount", ("#", "0"), ("L", "S"))

    # 6. Za jedno písmeno T1 přičti jednu. Nejméně významný bit je na T2 vlevo.
    for symbol in LETTERS:
        add("qCount", (symbol, "0"), "qCounterReturn", (symbol, "1"), ("S", "L"))
        add("qCount", (symbol, "1"), "qCarry", (symbol, "0"), ("S", "R"))
        add("qCarry", (symbol, "1"), "qCarry", (symbol, "0"), ("S", "R"))
        for bit in ("0", "#"):
            add("qCarry", (symbol, bit), "qCounterReturn", (symbol, "1"), ("S", "L"))
        for bit in ("0", "1"):
            add("qCounterReturn", (symbol, bit), "qCounterReturn", (symbol, bit), ("S", "L"))
        add("qCounterReturn", (symbol, "a"), "qCount", (symbol, "a"), ("L", "R"))

    # 7. T1 vrať na konec slova. Ponech jeden blank a přenes čítač v opačném pořadí.
    for bit in ("0", "1"):
        add("qCount", ("#", bit), "qSeekOutputEnd", ("#", bit), ("R", "S"))
        for symbol in LETTERS:
            add("qSeekOutputEnd", (symbol, bit), "qSeekOutputEnd", (symbol, bit), ("R", "S"))
        add("qSeekOutputEnd", ("#", bit), "qSeekCounterEnd", ("#", bit), ("R", "S"))
        add("qSeekCounterEnd", ("#", bit), "qSeekCounterEnd", ("#", bit), ("S", "R"))
        add("qCopyBits", ("#", bit), "qCopyBits", (bit, "#"), ("R", "L"))
    add("qSeekCounterEnd", ("#", "#"), "qCopyBits", ("#", "#"), ("S", "L"))

    # 8. Smaž poslední značku na T2. Obě pásky jsou v konečné konfiguraci.
    add("qCopyBits", ("#", "a"), "qHalt", ("#", "#"), ("S", "R"))
    return frozenset(states), tuple(transitions)


EXERCISE_STATES, EXERCISE_TRANSITIONS = _build_definition()


def make_exercise_machine(input_word: str = REQUIRED_INPUT) -> Machine:
    """Vloží původní slovo beze změn; číslo první pozice je 1 (liché)."""
    if any(symbol not in INPUT_ALPHABET for symbol in input_word):
        raise ValueError("Vstup stroje ze cvičení smí obsahovat pouze a, b, c, d, e.")
    return Machine(
        k=2,
        states=EXERCISE_STATES,
        transitions=EXERCISE_TRANSITIONS,
        initial_state=State("qStart"),
        halt_states={State("qHalt")},
        tapes=(Tape(input_word), Tape()),
    )
