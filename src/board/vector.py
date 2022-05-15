from __future__ import annotations


class BoardVector:
    def __init__(self, x, y):
        self._x: int = x
        self._y: int = y

    def __eq__(self, other):
        if isinstance(other, BoardVector):
            return self.x == other.x and self.y == other.y
        return False

    def __hash__(self):
        return hash((self.x, self.y))

    def __add__(self, other: BoardVector):
        return BoardVector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"vector({self.x}, {self.y})"

    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y

    def pair(self) -> tuple[int, int]:
        return self.x, self.y


vector = BoardVector  # alias for BoardVector
