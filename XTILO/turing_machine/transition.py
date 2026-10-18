"""Datová reprezentace jednoho přechodu δ(q, a) = (q', b, D)."""

from dataclasses import dataclass
from typing import Literal

from .state import State


Direction = Literal["L", "R", "S"]


@dataclass(frozen=True)
class Transition:
    state: State
    read_symbol: str
    next_state: State
    write_symbol: str
    operation: Direction

    def __post_init__(self) -> None:
        if len(self.read_symbol) != 1 or len(self.write_symbol) != 1:
            raise ValueError("Čtený a zapisovaný symbol musí mít právě jeden znak.")
        if self.operation not in ("L", "R", "S"):
            raise ValueError("Operace přechodu musí být L, R nebo S.")
