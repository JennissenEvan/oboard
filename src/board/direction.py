from __future__ import annotations

from enum import Enum
from functools import cached_property
from .board import vector


class Direction(Enum):
    N = 0
    NE = 1
    E = 2
    SE = 3
    S = 4
    SW = 5
    W = 6
    NW = 7

    @cached_property
    def vector(self):
        if "E" in self.name:
            xd = 1
        elif "W" in self.name:
            xd = -1
        else:
            xd = 0

        if "N" in self.name:
            yd = -1
        elif "S" in self.name:
            yd = 1
        else:
            yd = 0

        return vector(xd, yd)

    @cached_property
    def inverse(self):
        return self - 4

    @cached_property
    def degree(self):
        return 45 * self.value

    def __add__(self, other: int):
        return Direction((self.value + other) % 8)

    def __sub__(self, other: int):
        return Direction((self.value - other) % 8)
