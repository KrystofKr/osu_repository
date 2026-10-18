"""Studijní simulátor deterministického k-páskového Turingova stroje."""

from .machine import Machine, MissingTransitionError, RunResult, StepLimitExceeded, TapeResult
from .state import State
from .tape import Tape
from .transition import Direction, Transition

__all__ = [
    "Direction", "Machine", "MissingTransitionError", "RunResult",
    "State", "StepLimitExceeded", "Tape", "TapeResult", "Transition",
]
