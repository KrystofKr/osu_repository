"""Příkazová řádka pro kopírování a povinné dvoupáskové cvičení."""

import argparse

from .machine import MissingTransitionError, StepLimitExceeded
from .machines.copy_machine import make_copy_machine
from .machines.exercise_machine import make_exercise_machine


def main() -> None:
    parser = argparse.ArgumentParser(description="Simulátor k-páskového Turingova stroje")
    parser.add_argument("machine", choices=("copy", "exercise"), help="Konkrétní stroj")
    parser.add_argument("input", nargs="?", help="Vstup; bez něj abc nebo povinný vstup cvičení")
    parser.add_argument("--trace", action="store_true", help="Vypsat každý přechod a všechny pásky")
    parser.add_argument("--max-steps", type=int, default=100_000, help="Limit nových kroků")
    args = parser.parse_args()
    factory = make_copy_machine if args.machine == "copy" else make_exercise_machine
    try:
        machine = factory() if args.input is None else factory(args.input)
        result = machine.run(max_steps=args.max_steps, trace=args.trace)
    except (ValueError, MissingTransitionError, StepLimitExceeded) as error:
        parser.exit(1, f"Chyba: {error}\n")

    print(f"Konečný stav: {result.final_state}")
    print(f"steps = {result.step_count}")
    for number, tape in enumerate(result.tapes, start=1):
        print(f"T{number} content = {tape.tape_content!r}")
        print(f"T{number} head = {tape.head}")
        print(f"T{number} visited range = [{tape.leftmost_visited}, {tape.rightmost_visited}]")
        print(f"T{number} used cells = {tape.visited_cells}")
    print(f"total used cells = {result.total_used_cells}")
    print("Metrika: různé buňky navštívené hlavou, včetně blanků a počáteční pozice 0.")


if __name__ == "__main__":
    main()
