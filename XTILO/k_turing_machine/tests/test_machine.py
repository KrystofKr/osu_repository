"""Testy k-páskové infrastruktury na jednoduchých přechodových tabulkách."""

import io
import unittest
from contextlib import redirect_stdout

from .. import Machine, MissingTransitionError, State, StepLimitExceeded, Tape, Transition
from ..machines.copy_machine import make_copy_machine


class TapeTests(unittest.TestCase):
    def test_sparse_tape_negative_indices_and_visits(self) -> None:
        tape = Tape("a#b")
        self.assertEqual(tape.cells, {0: "a", 2: "b"})
        self.assertEqual(tape.visited_cell_count, 1)
        tape.move("L")
        self.assertEqual(tape.read(), "#")
        tape.write("c")
        self.assertEqual(tape.cells[-1], "c")
        for direction in ("R", "R", "R", "R", "S"):
            tape.move(direction)
        self.assertEqual((tape.head, tape.read()), (3, "#"))
        self.assertEqual((tape.leftmost_visited, tape.rightmost_visited), (-1, 3))
        self.assertEqual(tape.visited_cell_count, 5)

    def test_content_preserves_origin_and_internal_blank(self) -> None:
        tape = Tape()
        tape.move("R")
        tape.write("0")
        self.assertEqual(tape.content(), "#0")
        tape.write("#")
        self.assertEqual(tape.cells, {})
        self.assertEqual(tape.content(), "")

    def test_custom_blank_and_head_pointer(self) -> None:
        tape = Tape("a", blank_symbol="_")
        tape.move("L")
        self.assertEqual(tape.read(), "_")
        line, pointer = tape.render().splitlines()
        self.assertEqual(line[pointer.index("^")], "_")
        with self.assertRaises(ValueError):
            tape.write("ab")
        with self.assertRaises(ValueError):
            tape.move("X")  # type: ignore[arg-type]


class MachineTests(unittest.TestCase):
    def test_two_tape_copy(self) -> None:
        machine = make_copy_machine("abc")
        result = machine.run(max_steps=4)
        self.assertEqual(result.final_state, State("qHalt"))
        self.assertEqual(tuple(tape.tape_content for tape in result.tapes), ("abc", "abc"))
        self.assertEqual(result.step_count, 4)
        self.assertEqual(tuple(tape.head for tape in result.tapes), (3, 3))
        self.assertEqual(tuple(tape.visited_cells for tape in result.tapes), (4, 4))
        self.assertEqual(result.total_used_cells, 8)

    def test_independent_heads_move_right_and_left(self) -> None:
        start, halt = State("start"), State("halt")
        transition = Transition(start, ("a", "#"), halt, ("b", "c"), ("R", "L"))
        machine = Machine(2, {start, halt}, [transition], start, {halt}, (Tape("a"), Tape()))
        self.assertTrue(machine.step())
        self.assertEqual(tuple(tape.head for tape in machine.tapes), (1, -1))
        self.assertEqual(machine.tapes[0].cells, {0: "b"})
        self.assertEqual(machine.tapes[1].cells, {0: "c"})
        self.assertEqual(machine.step_count, 1)
        self.assertFalse(machine.step())
        self.assertEqual(machine.step_count, 1)

    def test_one_head_stays_while_other_moves(self) -> None:
        start, halt = State("start"), State("halt")
        machine = Machine(
            2, {start, halt},
            [Transition(start, ("a", "#"), halt, ("a", "b"), ("S", "R"))],
            start, {halt}, (Tape("a"), Tape()),
        )
        result = machine.run()
        self.assertEqual(tuple(tape.head for tape in result.tapes), (0, 1))
        self.assertEqual(tuple(tape.visited_cells for tape in result.tapes), (1, 2))

    def test_three_tapes_and_single_tape_are_supported(self) -> None:
        start, halt = State("start"), State("halt")
        machine = Machine(
            3, {start, halt},
            [Transition(start, ("a", "#", "#"), halt, ("a", "b", "c"), ("R", "L", "S"))],
            start, {halt}, (Tape("a"), Tape(), Tape()),
        )
        result = machine.run()
        self.assertEqual(tuple(tape.head for tape in result.tapes), (1, -1, 0))
        self.assertEqual(tuple(tape.tape_content for tape in result.tapes), ("a", "b", "c"))
        self.assertEqual(result.step_count, 1)
        self.assertEqual(result.total_used_cells, 5)
        single = Machine(
            1, {start, halt}, [Transition(start, ("#",), halt, ("a",), ("S",))],
            start, {halt}, (Tape(),),
        )
        self.assertEqual(single.run().tapes[0].tape_content, "a")

    def test_missing_transition_preserves_all_tapes(self) -> None:
        start, halt = State("start"), State("halt")
        machine = Machine(2, {start, halt}, [], start, {halt}, (Tape("a"), Tape("b")))
        with self.assertRaisesRegex(MissingTransitionError, "start.*'a', 'b'.*0, 0"):
            machine.run()
        self.assertEqual(machine.state, start)
        self.assertEqual(machine.step_count, 0)
        self.assertEqual(tuple(tape.cells for tape in machine.tapes), ({0: "a"}, {0: "b"}))

    def test_max_steps_stops_an_infinite_machine(self) -> None:
        loop = State("loop")
        machine = Machine(
            2, {loop}, [Transition(loop, ("#", "#"), loop, ("#", "#"), ("R", "L"))],
            loop, set(), (Tape(), Tape()),
        )
        with self.assertRaisesRegex(StepLimitExceeded, "7"):
            machine.run(max_steps=7)
        self.assertEqual(machine.step_count, 7)
        self.assertEqual(tuple(tape.head for tape in machine.tapes), (7, -7))
        self.assertFalse(machine.halted)

    def test_execution_resumes_with_new_limit(self) -> None:
        machine = make_copy_machine("abc")
        with self.assertRaises(StepLimitExceeded):
            machine.run(max_steps=2)
        result = machine.run(max_steps=2)
        self.assertEqual(result.step_count, 4)
        self.assertEqual(machine.run(max_steps=0), result)

    def test_zero_limit_initial_halt_and_invalid_limits(self) -> None:
        machine = make_copy_machine("a")
        with self.assertRaises(StepLimitExceeded):
            machine.run(max_steps=0)
        self.assertEqual(machine.step_count, 0)
        with self.assertRaises(ValueError):
            machine.run(max_steps=-1)
        for value in (True, 0.5):
            with self.subTest(value=value), self.assertRaises(TypeError):
                machine.run(max_steps=value)  # type: ignore[arg-type]
        halt = State("halt")
        stopped = Machine(2, {halt}, [], halt, {halt}, (Tape(), Tape()))
        self.assertEqual(stopped.run(max_steps=0).step_count, 0)

    def test_trace_contains_original_read_and_each_new_head(self) -> None:
        start, halt = State("start"), State("halt")
        machine = Machine(
            2, {start, halt},
            [Transition(start, ("a", "#"), halt, ("b", "c"), ("R", "L"))],
            start, {halt}, (Tape("a"), Tape()),
        )
        output = io.StringIO()
        with redirect_stdout(output):
            machine.run(trace=True)
        trace = output.getvalue()
        self.assertIn("step: 1\nstate: halt", trace)
        self.assertIn("read:  ('a', '#')", trace)
        self.assertIn("write: ('b', 'c')", trace)
        self.assertIn("move:  ('R', 'L')", trace)
        self.assertIn("T1: ##b###\n       ^\nhead: 1", trace)
        self.assertIn("T2: ###c##\n      ^\nhead: -1", trace)

    def test_duplicate_and_unknown_state_transitions_are_rejected(self) -> None:
        start, halt, unknown = State("start"), State("halt"), State("unknown")
        transition = Transition(start, ("#", "#"), halt, ("#", "#"), ("S", "S"))
        with self.assertRaisesRegex(ValueError, "Nedeterministická"):
            Machine(2, {start, halt}, [transition, transition], start, {halt}, (Tape(), Tape()))
        with self.assertRaises(ValueError):
            Machine(2, {start, halt}, [], unknown, {halt}, (Tape(), Tape()))
        with self.assertRaises(ValueError):
            Machine(2, {start, halt}, [], start, {unknown}, (Tape(), Tape()))
        with self.assertRaises(ValueError):
            Machine(
                2, {start, halt},
                [Transition(start, ("#", "#"), unknown, ("#", "#"), ("S", "S"))],
                start, {halt}, (Tape(), Tape()),
            )

    def test_invalid_k_tape_count_and_shared_tape(self) -> None:
        halt = State("halt")
        for k in (0, -1, True, 1.5):
            with self.subTest(k=k), self.assertRaises(ValueError):
                Machine(k, {halt}, [], halt, {halt}, ())  # type: ignore[arg-type]
        with self.assertRaises(ValueError):
            Machine(2, {halt}, [], halt, {halt}, (Tape(),))
        tape = Tape()
        with self.assertRaisesRegex(ValueError, "samostatný"):
            Machine(2, {halt}, [], halt, {halt}, (tape, tape))
        with self.assertRaises(ValueError):
            Machine(
                2, {halt}, [Transition(halt, ("#",), halt, ("#",), ("S",))],
                halt, {halt}, (Tape(), Tape()),
            )

    def test_invalid_transition_shape_and_symbols(self) -> None:
        state = State("q")
        cases = (
            ((), (), ()),
            (("#", "#"), ("#",), ("S", "S")),
            (("#", "#"), ("#", "#"), ("S",)),
            (("ab",), ("#",), ("S",)),
            (("#",), ("ab",), ("S",)),
            (("#",), ("#",), ("X",)),
        )
        for read, write, move in cases:
            with self.subTest(read=read, write=write, move=move), self.assertRaises(ValueError):
                Transition(state, read, state, write, move)  # type: ignore[arg-type]
        with self.assertRaises(TypeError):
            Transition(state, ["#"], state, ("#",), ("S",))  # type: ignore[arg-type]


if __name__ == "__main__":
    unittest.main()
