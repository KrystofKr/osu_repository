"""Stav deterministického Turingova stroje."""

from dataclasses import dataclass


@dataclass(frozen=True)
class State:
    id: str

    def __post_init__(self) -> None:
        if not self.id:
            raise ValueError("Identifikátor stavu nesmí být prázdný.")

    def __str__(self) -> str:
        return self.id
