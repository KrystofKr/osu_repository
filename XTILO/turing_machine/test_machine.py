"""Testy simulátoru a přechodové tabulky, pouze pomocí unittest."""

import io
import unittest
from contextlib import redirect_stdout

from . import Machine, MissingTransitionError, State, StepLimitExceeded, Tape, Transition
from .examples import (
    COMPARISON_TAPE_ALPHABET,
    COMPARISON_TRANSITIONS,
    make_comparator,
    make_scanner,
)


class TapeTests(unittest.TestCase):
    def test_initial_sparse_tape_and_unvisited_input(self) -> None:
        tape = Tape("10#1")
        self.assertEqual(tape.cells, {0: "1", 1: "0", 3: "1"})
        self.assertEqual(tape.head, 0)
        self.assertEqual(tape.read(), "1")
        self.assertEqual(tape.visited_cell_count, 1)
        self.assertEqual(tape.content(), "10#1")

    def test_movement_and_blank_on_both_sides(self) -> None:
        tape = Tape("1")
        tape.move("L")
        self.assertEqual((tape.head, tape.read()), (-1, "#"))
        tape.write("0")
        self.assertEqual(tape.cells[-1], "0")
        tape.move("R")
        tape.move("R")
        self.assertEqual((tape.head, tape.read()), (1, "#"))
        self.assertEqual((tape.leftmost_visited, tape.rightmost_visited), (-1, 1))
        self.assertEqual(tape.visited_cell_count, 3)
        tape.move("L")
        tape.move("S")
        self.assertEqual(tape.visited_cell_count, 3)

    def test_writing_blank_removes_cell(self) -> None:
        tape = Tape("1")
        tape.write("#")
        self.assertEqual(tape.cells, {})
        self.assertEqual(tape.read(), "#")
        self.assertEqual(tape.content(), "")

    def test_custom_blank_symbol(self) -> None:
        tape = Tape("a_a", blank_symbol="_")
        tape.move("R")
        self.assertEqual(tape.read(), "_")
        tape.write("b")
        self.assertEqual(tape.content(), "aba")
        tape.write("_")
        self.assertEqual(tape.content(), "a_a")

    def test_render_points_at_head_outside_content(self) -> None:
        tape = Tape("10")
        for direction in ("L", "R", "R", "R", "R"):
            tape.move(direction)
            line, pointer = tape.render().splitlines()
            self.assertEqual(line[pointer.index("^")], tape.read())
            self.assertIn("10", line)
        self.assertEqual(Tape().render(), "#####\n  ^")

    def test_invalid_symbols_and_direction(self) -> None:
        with self.assertRaises(ValueError):
            Tape(blank_symbol="")
        tape = Tape()
        with self.assertRaises(ValueError):
            tape.write("01")
        with self.assertRaises(ValueError):
            tape.move("X")  # type: ignore[arg-type]
        self.assertEqual(tape.head, 0)


class MachineTests(unittest.TestCase):
    def test_step_writes_changes_state_moves_and_counts(self) -> None:
        start, halt = State("start"), State("halt")
        machine = Machine(
            {start, halt}, [Transition(start, "1", halt, "0", "L")],
            start, {halt}, Tape("1"),
        )
        self.assertTrue(machine.step())
        self.assertEqual(machine.tape.cells, {0: "0"})
        self.assertEqual(machine.state, halt)
        self.assertEqual(machine.tape.head, -1)
        self.assertEqual(machine.step_count, 1)
        self.assertFalse(machine.step())
        self.assertEqual(machine.step_count, 1)

    def test_scanner_preserves_input_and_stops_on_blank(self) -> None:
        machine = make_scanner("1010")
        result = machine.run(max_steps=5)
        self.assertEqual(result.final_state, State("qHalt"))
        self.assertEqual(result.tape_content, "1010")
        self.assertEqual(result.step_count, 5)
        self.assertEqual(machine.tape.head, 4)
        self.assertEqual((result.leftmost_visited, result.rightmost_visited), (0, 4))
        self.assertEqual(result.visited_cells, 5)

    def test_empty_scanner(self) -> None:
        result = make_scanner("").run()
        self.assertEqual(result.tape_content, "")
        self.assertEqual(result.step_count, 1)
        self.assertEqual(result.visited_cells, 1)

    def test_missing_transition_does_not_modify_configuration(self) -> None:
        start, halt = State("start"), State("halt")
        machine = Machine({start, halt}, [], start, {halt}, Tape("a"))
        with self.assertRaisesRegex(MissingTransitionError, "start.*'a'.*0"):
            machine.run()
        self.assertEqual(machine.state, start)
        self.assertEqual(machine.tape.content(), "a")
        self.assertEqual(machine.tape.head, 0)
        self.assertEqual(machine.step_count, 0)

    def test_duplicate_transitions_are_rejected(self) -> None:
        start, halt = State("start"), State("halt")
        transitions = [
            Transition(start, "#", halt, "0", "S"),
            Transition(start, "#", halt, "1", "S"),
        ]
        with self.assertRaisesRegex(ValueError, "Nedeterministická"):
            Machine({start, halt}, transitions, start, {halt}, Tape())

    def test_unknown_states_are_rejected(self) -> None:
        start, halt, unknown = State("start"), State("halt"), State("unknown")
        with self.assertRaises(ValueError):
            Machine({start, halt}, [], unknown, {halt}, Tape())
        with self.assertRaises(ValueError):
            Machine({start, halt}, [], start, {unknown}, Tape())
        with self.assertRaises(ValueError):
            Machine(
                {start, halt}, [Transition(start, "#", unknown, "#", "S")],
                start, {halt}, Tape(),
            )

    def test_invalid_transition_and_state(self) -> None:
        start, halt = State("start"), State("halt")
        with self.assertRaises(ValueError):
            State("")
        with self.assertRaises(ValueError):
            Transition(start, "01", halt, "0", "R")
        with self.assertRaises(ValueError):
            Transition(start, "0", halt, "00", "R")
        with self.assertRaises(ValueError):
            Transition(start, "0", halt, "0", "X")  # type: ignore[arg-type]

    def test_step_limit_stops_infinite_loop(self) -> None:
        start = State("loop")
        machine = Machine(
            {start}, [Transition(start, "#", start, "#", "S")],
            start, set(), Tape(),
        )
        with self.assertRaisesRegex(StepLimitExceeded, "7"):
            machine.run(max_steps=7)
        self.assertEqual(machine.step_count, 7)
        self.assertFalse(machine.halted)

    def test_limit_is_per_run_and_execution_can_resume(self) -> None:
        machine = make_scanner("10")
        with self.assertRaises(StepLimitExceeded):
            machine.run(max_steps=2)
        self.assertEqual(machine.step_count, 2)
        result = machine.run(max_steps=1)
        self.assertEqual(result.step_count, 3)
        self.assertEqual(machine.run(max_steps=0), result)

    def test_zero_limit_and_invalid_limits(self) -> None:
        machine = make_scanner("1")
        with self.assertRaises(StepLimitExceeded):
            machine.run(max_steps=0)
        self.assertEqual(machine.step_count, 0)
        with self.assertRaises(ValueError):
            machine.run(max_steps=-1)
        for value in (1.5, True):
            with self.subTest(value=value), self.assertRaises(TypeError):
                machine.run(max_steps=value)  # type: ignore[arg-type]

    def test_initial_halt_state_needs_no_transition(self) -> None:
        halt = State("halt")
        machine = Machine({halt}, [], halt, {halt}, Tape("1"))
        result = machine.run(max_steps=0)
        self.assertEqual(result.step_count, 0)
        self.assertEqual(result.tape_content, "1")

    def test_trace_is_printed_after_each_step(self) -> None:
        output = io.StringIO()
        with redirect_stdout(output):
            make_scanner("1").run(trace=True)
        trace = output.getvalue()
        self.assertEqual(trace.count("step:"), 2)
        self.assertIn("step: 1\nstate: qScan\nhead: 1\nread: #", trace)
        self.assertIn("step: 2\nstate: qHalt\nhead: 1\nread: #", trace)
        self.assertIn("tape:\n##1###\n   ^", trace)

    def test_scanner_rejects_nonbinary_input(self) -> None:
        with self.assertRaises(ValueError):
            make_scanner("10>1")


class ComparisonTests(unittest.TestCase):
    def test_assignment_examples(self) -> None:
        for word, expected in (("100>10", "1"), ("10>10", "0"), ("1>10", "0")):
            with self.subTest(word=word):
                machine = make_comparator(word)
                result = machine.run()
                self.assertEqual(result.tape_content, expected)
                self.assertEqual(machine.tape.cells, {0: expected})
                self.assertEqual(machine.tape.head, 0)
                self.assertEqual(result.final_state, State("qHalt"))
                self.assertEqual(result.leftmost_visited, -1)
                self.assertEqual(result.rightmost_visited, len(word))
                self.assertEqual(result.visited_cells, len(word) + 2)

    def test_leading_zeros_and_zero_operands(self) -> None:
        cases = (
            ("00100>00010", "1"), ("010>00010", "0"), ("0001>010", "0"),
            ("0>0", "0"), ("1>0", "1"), ("0>1", "0"), ("000>00", "0"),
            ("1000000000000000>1", "1"), ("1>1000000000000000", "0"),
        )
        for word, expected in cases:
            with self.subTest(word=word):
                self.assertEqual(make_comparator(word).run().tape_content, expected)

    def test_all_small_pairs_with_and_without_leading_zeros(self) -> None:
        # Pythonové porovnání slouží pouze jako nezávislý testovací oracle.
        # Simulátor ani definice stroje číselné hodnoty v Pythonu nepočítají.
        for left in range(16):
            for right in range(16):
                expected = "1" if left > right else "0"
                prefixes = (("", ""), ("00", ""), ("", "00"), ("00", "00"))
                for left_prefix, right_prefix in prefixes:
                    word = f"{left_prefix}{left:b}>{right_prefix}{right:b}"
                    with self.subTest(word=word):
                        self.assertEqual(make_comparator(word).run().tape_content, expected)

    def test_transitions_use_only_required_tape_alphabet(self) -> None:
        self.assertEqual(COMPARISON_TAPE_ALPHABET, {"0", "1", ">", "#"})
        for transition in COMPARISON_TRANSITIONS:
            self.assertIn(transition.read_symbol, COMPARISON_TAPE_ALPHABET)
            self.assertIn(transition.write_symbol, COMPARISON_TAPE_ALPHABET)

    def test_invalid_comparison_input(self) -> None:
        for word in ("", "10", ">1", "1>", "1>>1", "1>1>1", "2>1", "1>#", "1 >1"):
            with self.subTest(word=word), self.assertRaisesRegex(ValueError, "tvar x>y"):
                make_comparator(word)


if __name__ == "__main__":
    unittest.main()
