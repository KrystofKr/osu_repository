"""Obecný deterministický k-páskový simulátor, bez logiky konkrétní úlohy."""

from collections.abc import Iterable
from dataclasses import dataclass

from .state import State
from .tape import Tape
from .transition import Transition


class MissingTransitionError(RuntimeError):
    """Pro aktuální stav a přečtenou n-tici není definován přechod."""


class StepLimitExceeded(RuntimeError):
    """Běh vyčerpal povolený počet přechodů."""


@dataclass(frozen=True)
class TapeResult:
    tape_content: str
    head: int
    leftmost_visited: int
    rightmost_visited: int
    visited_cells: int


@dataclass(frozen=True)
class RunResult:
    final_state: State
    step_count: int
    tapes: tuple[TapeResult, ...]
    total_used_cells: int


class Machine:
    def __init__(
        self,
        k: int,
        states: Iterable[State],
        transitions: Iterable[Transition],
        initial_state: State,
        halt_states: Iterable[State],
        tapes: Iterable[Tape],
    ) -> None:
        if not isinstance(k, int) or isinstance(k, bool) or k < 1:
            raise ValueError("Počet pásek k musí být kladné celé číslo.")
        self.k = k
        self.tapes = tuple(tapes)
        if len(self.tapes) != k:
            raise ValueError(f"Stroj s k={k} potřebuje právě {k} pásek.")
        if len({id(tape) for tape in self.tapes}) != k:
            raise ValueError("Každá páska musí být samostatný objekt Tape.")
        self.states = frozenset(states)
        self.halt_states = frozenset(halt_states)
        if initial_state not in self.states:
            raise ValueError("Počáteční stav musí patřit do množiny stavů.")
        if not self.halt_states <= self.states:
            raise ValueError("Koncové stavy musí patřit do množiny stavů.")

        self.transitions: dict[tuple[State, tuple[str, ...]], Transition] = {}
        for transition in transitions:
            if len(transition.read_symbols) != k:
                raise ValueError(f"Každý přechod musí popisovat právě {k} pásek.")
            if (
                transition.state not in self.states
                or transition.next_state not in self.states
            ):
                raise ValueError("Každý přechod musí odkazovat na definované stavy.")
            key = (transition.state, transition.read_symbols)
            if key in self.transitions:
                raise ValueError(
                    f"Nedeterministická definice: více přechodů pro "
                    f"({transition.state}, {transition.read_symbols!r})."
                )
            self.transitions[key] = transition

        self.state = initial_state
        self.step_count = 0

    @property
    def halted(self) -> bool:
        return self.state in self.halt_states

    def find_transition(self) -> Transition:
        read_symbols = tuple(tape.read() for tape in self.tapes)
        transition = self.transitions.get((self.state, read_symbols))
        if transition is None:
            heads = tuple(tape.head for tape in self.tapes)
            raise MissingTransitionError(
                f"Chybí přechod pro stav {self.state}, symboly {read_symbols!r} "
                f"a pozice hlav {heads}."
            )
        return transition

    def execute_transition(self, transition: Transition) -> None:
        for tape, symbol in zip(self.tapes, transition.write_symbols):
            tape.write(symbol)
        for tape, direction in zip(self.tapes, transition.operations):
            tape.move(direction)
        self.state = transition.next_state
        self.step_count += 1

    def step(self) -> bool:
        """Provede jeden společný přechod; v koncovém stavu nic nemění."""
        if self.halted:
            return False
        transition = self.find_transition()
        self.execute_transition(transition)
        return True

    def print_trace(self, transition: Transition) -> None:
        """Nová konfigurace pásek a údaje právě provedeného přechodu."""
        print(
            f"step: {self.step_count}\n"
            f"state: {self.state}\n"
            f"read:  {transition.read_symbols!r}\n"
            f"write: {transition.write_symbols!r}\n"
            f"move:  {transition.operations!r}\n"
        )
        for number, tape in enumerate(self.tapes, start=1):
            line, pointer = tape.render().splitlines()
            label = f"T{number}: "
            print(f"{label}{line}\n{' ' * len(label)}{pointer}\nhead: {tape.head}\n")

    def run(self, max_steps: int = 100_000, trace: bool = False) -> RunResult:
        """Limit platí pro nové přechody v tomto volání; čítač je kumulativní."""
        if not isinstance(max_steps, int) or isinstance(max_steps, bool):
            raise TypeError("max_steps musí být celé číslo.")
        if max_steps < 0:
            raise ValueError("max_steps nesmí být záporné.")
        steps_at_start = self.step_count
        while not self.halted:
            if self.step_count - steps_at_start >= max_steps:
                raise StepLimitExceeded(
                    f"Vyčerpán limit {max_steps} kroků tohoto běhu; "
                    f"celkem {self.step_count} kroků, stav {self.state}."
                )
            # Pro trasování zachováme čtení původní konfigurace.
            transition = self.find_transition() if trace else None
            self.step()
            if transition is not None:
                self.print_trace(transition)
        tape_results = tuple(
            TapeResult(
                tape_content=tape.content(),
                head=tape.head,
                leftmost_visited=tape.leftmost_visited,
                rightmost_visited=tape.rightmost_visited,
                visited_cells=tape.visited_cell_count,
            )
            for tape in self.tapes
        )
        return RunResult(
            final_state=self.state,
            step_count=self.step_count,
            tapes=tape_results,
            total_used_cells=sum(tape.visited_cells for tape in tape_results),
        )
