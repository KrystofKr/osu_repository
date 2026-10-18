"""Ručně zadané výsledky; testy nefiltrují, netřídí ani nepočítají vstup."""

import unittest

from .. import State, StepLimitExceeded
from ..machines.exercise_machine import (
    EXERCISE_TRANSITIONS,
    INPUT_ALPHABET,
    REQUIRED_INPUT,
    TAPE_ALPHABET,
    make_exercise_machine,
)


class ExerciseMachineTests(unittest.TestCase):
    def assert_output(self, word: str, expected: str) -> None:
        machine = make_exercise_machine(word)
        result = machine.run(max_steps=10_000)
        self.assertEqual(result.final_state, State("qHalt"))
        self.assertEqual(result.tapes[0].tape_content, expected)
        # Ověříme skutečné buňky včetně pozice oddělovače a nepřítomnosti značek.
        expected_cells = {
            position: symbol
            for position, symbol in enumerate(expected)
            if symbol != "#"
        }
        self.assertEqual(machine.tapes[0].cells, expected_cells)
        self.assertEqual(machine.tapes[1].cells, {})
        self.assertEqual(result.tapes[1].tape_content, "")
        self.assertEqual(result.tapes[1].head, 0)

    def test_required_input(self) -> None:
        # Potvrzené mazání na pozicích 2, 4, ...; čtyři a, celkem 19 písmen.
        self.assert_output(REQUIRED_INPUT, "aaaabbbccccdddeeeee#10011")
        result = make_exercise_machine().run()
        self.assertEqual(
            (result.tapes[0].leftmost_visited, result.tapes[0].rightmost_visited), (-1, 25),
        )
        self.assertEqual(
            (result.tapes[1].leftmost_visited, result.tapes[1].rightmost_visited), (-1, 19),
        )
        self.assertEqual(tuple(tape.visited_cells for tape in result.tapes), (27, 21))
        self.assertEqual(result.total_used_cells, 48)

    def test_empty_and_single_symbol_words(self) -> None:
        for word, expected in (
            ("", "#0"), ("a", "a#1"), ("b", "b#1"),
            ("c", "c#1"), ("d", "d#1"), ("e", "e#1"),
        ):
            with self.subTest(word=word):
                self.assert_output(word, expected)

    def test_deletion_uses_original_positions(self) -> None:
        cases = (
            ("aa", "a#1"), ("ee", "e#1"), ("ae", "a#1"), ("ea", "e#1"),
            ("aea", "aa#10"), ("eae", "ee#10"),
            ("aaaa", "aa#10"), ("eeee", "ee#10"),
            ("baca", "bc#10"), ("baea", "be#10"), ("abea", "abe#11"),
            ("abababa", "aaaabbb#111"), ("bcdea", "abcd#100"),
        )
        for word, expected in cases:
            with self.subTest(word=word):
                self.assert_output(word, expected)

    def test_sorting_and_absent_letter_groups(self) -> None:
        for word, expected in (
            ("edcba", "abcde#101"), ("edcbab", "abbcde#110"),
            ("ccbbdd", "bbccdd#110"), ("dddd", "dddd#100"),
            ("deea", "de#10"), ("dbcae", "bcde#100"),
        ):
            with self.subTest(word=word):
                self.assert_output(word, expected)

    def test_binary_counter_carries_and_output_can_grow(self) -> None:
        cases = (
            ("bbb", "bbb#11"),
            ("bbbb", "bbbb#100"),
            ("bbbbbbb", "bbbbbbb#111"),
            ("bbbbbbbb", "bbbbbbbb#1000"),
            ("bbbbbbbbbbbbbbb", "bbbbbbbbbbbbbbb#1111"),
            ("bbbbbbbbbbbbbbbb", "bbbbbbbbbbbbbbbb#10000"),
        )
        for word, expected in cases:
            with self.subTest(word=word):
                self.assert_output(word, expected)

    def test_intermediate_tapes_follow_the_documented_phases(self) -> None:
        machine = make_exercise_machine("baea")

        def advance_to(state_id: str) -> None:
            for _ in range(500):
                if machine.state.id == state_id:
                    return
                self.assertTrue(machine.step())
            self.fail(f"Stroj nedošel do {state_id}.")

        advance_to("qSelect_a")
        self.assertEqual(machine.tapes[0].cells, {})
        self.assertEqual(machine.tapes[1].cells, {-1: "1", 0: "b", 1: "e", 2: "0"})
        advance_to("qInitCounterMarker")
        self.assertEqual(machine.tapes[0].cells, {0: "b", 1: "e"})
        self.assertEqual(machine.tapes[1].cells, {})
        advance_to("qSeekOutputEnd")
        # Čítač hodnoty dva: nejméně významný bit je vlevo, tedy 01.
        self.assertEqual(machine.tapes[1].cells, {-1: "a", 0: "0", 1: "1"})
        self.assertEqual(machine.run().tapes[0].tape_content, "be#10")
        self.assertEqual(machine.tapes[1].cells, {})

    def test_only_allowed_symbols_are_used_in_every_step(self) -> None:
        self.assertEqual(INPUT_ALPHABET, {"a", "b", "c", "d", "e"})
        self.assertEqual(TAPE_ALPHABET, {"a", "b", "c", "d", "e", "0", "1", "#"})
        for transition in EXERCISE_TRANSITIONS:
            self.assertTrue(set(transition.read_symbols) <= TAPE_ALPHABET)
            self.assertTrue(set(transition.write_symbols) <= TAPE_ALPHABET)
        machine = make_exercise_machine()
        for _ in range(1000):
            if machine.halted:
                break
            machine.step()
            for tape in machine.tapes:
                self.assertTrue(set(tape.cells.values()) <= TAPE_ALPHABET)
        else:
            self.fail("Povinný vstup nedoběhl během 1000 přechodů.")

    def test_factory_preserves_input_and_rejects_wrong_alphabet(self) -> None:
        machine = make_exercise_machine("edcba")
        self.assertEqual(machine.tapes[0].cells, {0: "e", 1: "d", 2: "c", 3: "b", 4: "a"})
        self.assertEqual(machine.tapes[1].cells, {})
        self.assertEqual(machine.step_count, 0)
        for word in ("a#b", "abc0", "abc1", "abf", "a e"):
            with self.subTest(word=word), self.assertRaises(ValueError):
                make_exercise_machine(word)

    def test_limited_exercise_can_resume(self) -> None:
        machine = make_exercise_machine("baea")
        with self.assertRaises(StepLimitExceeded):
            machine.run(max_steps=5)
        self.assertEqual(machine.step_count, 5)
        self.assertEqual(machine.run().tapes[0].tape_content, "be#10")


if __name__ == "__main__":
    unittest.main()
