"""Spouštění příkladů: python3 -m turing_machine scan/compare VSTUP."""

import argparse

from .examples import make_comparator, make_scanner
from .machine import MissingTransitionError, StepLimitExceeded


def main() -> None:
    parser = argparse.ArgumentParser(description="Simulátor Turingova stroje")
    parser.add_argument("machine", choices=("scan", "compare"), help="Ukázkový stroj")
    parser.add_argument("input", help="Binární slovo nebo výraz x>y (uzavřete do uvozovek)")
    parser.add_argument("--trace", action="store_true", help="Vypisovat konfiguraci po každém kroku")
    parser.add_argument("--max-steps", type=int, default=100_000, help="Limit kroků (výchozí: 100000)")
    args = parser.parse_args()
    factory = make_scanner if args.machine == "scan" else make_comparator
    try:
        machine = factory(args.input)
        result = machine.run(max_steps=args.max_steps, trace=args.trace)
    except (ValueError, MissingTransitionError, StepLimitExceeded) as error:
        parser.exit(1, f"Chyba: {error}\n")

    print(f"Konečný stav: {result.final_state}")
    print(f"Počet kroků: {result.step_count}")
    print(f"Obsah pásky: {result.tape_content!r}")
    print(f"Nejlevější navštívená buňka: {result.leftmost_visited}")
    print(f"Nejpravější navštívená buňka: {result.rightmost_visited}")
    print(f"Počet navštívených buněk: {result.visited_cells}")


if __name__ == "__main__":
    main()
