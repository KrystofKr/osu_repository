"""Jednoduchý dvoupáskový stroj kopírující T1 na T2."""

from .. import Machine, State, Tape, Transition


COPY_ALPHABET = ("a", "b", "c", "d", "e")
COPY_STATE, COPY_HALT = State("qCopy"), State("qHalt")
COPY_TRANSITIONS = tuple(
    Transition(COPY_STATE, (symbol, "#"), COPY_STATE, (symbol, symbol), ("R", "R"))
    for symbol in COPY_ALPHABET
) + (
    Transition(COPY_STATE, ("#", "#"), COPY_HALT, ("#", "#"), ("S", "S")),
)


def make_copy_machine(input_word: str = "abc") -> Machine:
    if any(symbol not in COPY_ALPHABET for symbol in input_word):
        raise ValueError("Vstup kopírovacího stroje smí obsahovat pouze a, b, c, d, e.")
    return Machine(
        k=2,
        states={COPY_STATE, COPY_HALT},
        transitions=COPY_TRANSITIONS,
        initial_state=COPY_STATE,
        halt_states={COPY_HALT},
        tapes=(Tape(input_word), Tape()),
    )
