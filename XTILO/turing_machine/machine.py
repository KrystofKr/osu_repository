"""Obecný simulátor: o konkrétním problému rozhodují pouze přechody."""

from collections.abc import Iterable
from dataclasses import dataclass

from .state import State
from .tape import Tape
from .transition import Transition


class MissingTransitionError(RuntimeError):
    """Stroj není koncový, ale pro aktuální konfiguraci nemá přechod."""


class StepLimitExceeded(RuntimeError):
    """Běh vyčerpal povolený počet přechodů."""


@dataclass(frozen=True)
class RunResult:
    final_state: State
    step_count: int
    tape_content: str
    leftmost_visited: int
    rightmost_visited: int
    visited_cells: int


class Machine:
    def __init__(
        self,
        states: Iterable[State],
        transitions: Iterable[Transition],
        initial_state: State,
        halt_states: Iterable[State],
        tape: Tape,
    ) -> None:
        self.states = frozenset(states)
        self.halt_states = frozenset(halt_states)
        if initial_state not in self.states:
            raise ValueError("Počáteční stav musí patřit do množiny stavů.")
        if not self.halt_states <= self.states:
            raise ValueError("Koncové stavy musí patřit do množiny stavů.")

        self.transitions: dict[tuple[State, str], Transition] = {}
        for transition in transitions:
            if (
                transition.state not in self.states
                or transition.next_state not in self.states
            ):
                raise ValueError("Každý přechod musí odkazovat na definované stavy.")
            key = (transition.state, transition.read_symbol)
            if key in self.transitions:
                raise ValueError(
                    f"Nedeterministická definice: více přechodů pro "
                    f"({transition.state}, {transition.read_symbol!r})."
                )
            self.transitions[key] = transition

        self.state = initial_state
        self.tape = tape
        self.step_count = 0

    @property
    def halted(self) -> bool:
        return self.state in self.halt_states

    def find_transition(self) -> Transition:
        symbol = self.tape.read()
        transition = self.transitions.get((self.state, symbol))
        if transition is None:
            raise MissingTransitionError(
                f"Chybí přechod pro stav {self.state}, symbol {symbol!r} "
                f"a pozici hlavy {self.tape.head}."
            )
        return transition

    def execute_transition(self, transition: Transition) -> None:
        self.tape.write(transition.write_symbol)
        self.state = transition.next_state
        self.tape.move(transition.operation)
        self.step_count += 1

    def step(self) -> bool:
        """Provede jeden přechod; v koncovém stavu vrátí False beze změn."""
        if self.halted:
            return False
        transition = self.find_transition()
        self.execute_transition(transition)
        return True

    def run(self, max_steps: int = 100_000, trace: bool = False) -> RunResult:
        """Provede nejvýše max_steps nových přechodů během tohoto volání."""
        if not isinstance(max_steps, int) or isinstance(max_steps, bool):
            raise TypeError("max_steps musí být celé číslo.")
        if max_steps < 0:
            raise ValueError("max_steps nesmí být záporné.")
        steps_at_start = self.step_count
        while not self.halted:
            if self.step_count - steps_at_start >= max_steps:
                raise StepLimitExceeded(
                    f"Vyčerpán limit {max_steps} kroků tohoto běhu; "
                    f"celkem {self.step_count} kroků, stav {self.state}, "
                    f"pozice hlavy {self.tape.head}."
                )
            self.step()
            if trace:
                print(
                    f"step: {self.step_count}\n"
                    f"state: {self.state}\n"
                    f"head: {self.tape.head}\n"
                    f"read: {self.tape.read()}\n"
                    f"tape:\n{self.tape.render()}\n"
                )
        return RunResult(
            final_state=self.state,
            step_count=self.step_count,
            tape_content=self.tape.content(),
            leftmost_visited=self.tape.leftmost_visited,
            rightmost_visited=self.tape.rightmost_visited,
            visited_cells=self.tape.visited_cell_count,
        )
