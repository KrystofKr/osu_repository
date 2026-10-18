"""Řídká páska neomezená v obou směrech."""

from .transition import Direction


class Tape:
    def __init__(self, input_word: str = "", blank_symbol: str = "#") -> None:
        if len(blank_symbol) != 1:
            raise ValueError("Blank symbol musí mít právě jeden znak.")
        self.blank_symbol = blank_symbol
        self.cells: dict[int, str] = {
            position: symbol
            for position, symbol in enumerate(input_word)
            if symbol != blank_symbol
        }
        self.head = 0
        self.leftmost_visited = 0
        self.rightmost_visited = 0

    def read(self) -> str:
        return self.cells.get(self.head, self.blank_symbol)

    def write(self, symbol: str) -> None:
        if len(symbol) != 1:
            raise ValueError("Zapisovaný symbol musí mít právě jeden znak.")
        if symbol == self.blank_symbol:
            self.cells.pop(self.head, None)
        else:
            self.cells[self.head] = symbol

    def move(self, direction: Direction) -> None:
        if direction == "L":
            self.head -= 1
        elif direction == "R":
            self.head += 1
        elif direction != "S":
            raise ValueError("Směr pohybu musí být L, R nebo S.")
        self.leftmost_visited = min(self.leftmost_visited, self.head)
        self.rightmost_visited = max(self.rightmost_visited, self.head)

    @property
    def visited_cell_count(self) -> int:
        # Hlava se pohybuje po jedné buňce, navštívené pozice tvoří interval.
        return self.rightmost_visited - self.leftmost_visited + 1

    def content(self) -> str:
        """Obsah mezi krajními neblankovými buňkami včetně vnitřních blanků."""
        if not self.cells:
            return ""
        return "".join(
            self.cells.get(position, self.blank_symbol)
            for position in range(min(self.cells), max(self.cells) + 1)
        )

    def render(self, padding: int = 2) -> str:
        """Páska a ukazatel hlavy; zobrazí se i hlava mimo uložené buňky."""
        if padding < 0:
            raise ValueError("Počet okrajových blanků nesmí být záporný.")
        left = min(self.head, min(self.cells, default=self.head)) - padding
        right = max(self.head, max(self.cells, default=self.head)) + padding
        line = "".join(
            self.cells.get(position, self.blank_symbol)
            for position in range(left, right + 1)
        )
        return line + "\n" + " " * (self.head - left) + "^"
