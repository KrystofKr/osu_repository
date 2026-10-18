"""Neměnný přechod, který současně pracuje se všemi k páskami."""

from dataclasses import dataclass
from typing import Literal

from .state import State


Direction = Literal["L", "R", "S"]


@dataclass(frozen=True)
class Transition:
    state: State
    read_symbols: tuple[str, ...]
    next_state: State
    write_symbols: tuple[str, ...]
    operations: tuple[Direction, ...]

    def __post_init__(self) -> None:
        if not all(isinstance(value, tuple) for value in (
            self.read_symbols, self.write_symbols, self.operations,
        )):
            raise TypeError("Symboly a operace přechodu musí být neměnné n-tice.")
        if not self.read_symbols or not (
            len(self.read_symbols) == len(self.write_symbols) == len(self.operations)
        ):
            raise ValueError("Přechod musí mít stejný nenulový počet čtení, zápisů a pohybů.")
        if any(len(symbol) != 1 for symbol in self.read_symbols + self.write_symbols):
            raise ValueError("Každý čtený a zapisovaný symbol musí mít právě jeden znak.")
        if any(operation not in ("L", "R", "S") for operation in self.operations):
            raise ValueError("Každá operace přechodu musí být L, R nebo S.")
