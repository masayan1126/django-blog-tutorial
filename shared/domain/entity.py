from typing import Final


class Entity:
    id: Final[int]

    def __init__(self, id: int):
        self.id = id

    def equals(self, other):
        return self.id == other.id
