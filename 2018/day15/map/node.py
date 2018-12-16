from typing import Tuple

class BaseNode:
    def __init__(self, map, x: int, y: int, type: str):
        self.map = map
        self.x = x
        self.y = y
        self.type = type

        self.map[(x, y)] = self

    def __str__(self):
        return '({}, {}): {}'.format(self.x, self.y, self.type)

    def __gt__(self, other):
        return (self.y, self.x) > (other.y, other.x)

    def __lt__(self, other):
        return (self.y, self.x) < (other.y, other.x)

class Node(BaseNode):

    @property
    def up(self) -> BaseNode:
        return self.map[(self.x, self.y - 1)]

    @property
    def down(self) -> BaseNode:
        return self.map[(self.x, self.y + 1)]

    @property
    def left(self) -> BaseNode:
        return self.map[(self.x - 1, self.y)]

    @property
    def right(self) -> BaseNode:
        return self.map[(self.x + 1, self.y)]

    @property
    def adj(self) -> Tuple[BaseNode]:
        return (self.up, self.left, self.down, self.right)
