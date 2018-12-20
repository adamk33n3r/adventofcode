from typing import Tuple

class BaseNode:
    def __init__(self, map, x: int, y: int, type: str):
        self.map = map
        self.x = x
        self.y = y
        self.type = type

        self.map[(x, y)] = self

    @property
    def pos(self):
        return (self.x, self.y)

    def __str__(self):
        return '({}, {}): {}'.format(self.x, self.y, self.type)

    def __gt__(self, other):
        return (self.y, self.x) > (other.y, other.x)

    def __lt__(self, other):
        return (self.y, self.x) < (other.y, other.x)

class Node(BaseNode):

    @property
    def up(self) -> BaseNode:
        return self.map.get((self.x, self.y - 1), None)

    @property
    def down(self) -> BaseNode:
        return self.map.get((self.x, self.y + 1), None)

    @property
    def left(self) -> BaseNode:
        return self.map.get((self.x - 1, self.y), None)

    @property
    def right(self) -> BaseNode:
        return self.map.get((self.x + 1, self.y), None)

    @property
    def rightDown(self) -> BaseNode:
        return self.map.get((self.x + 1, self.y + 1), None)

    @property
    def rightUp(self) -> BaseNode:
        return self.map.get((self.x + 1, self.y - 1), None)

    @property
    def leftDown(self) -> BaseNode:
        return self.map.get((self.x - 1, self.y + 1), None)

    @property
    def leftUp(self) -> BaseNode:
        return self.map.get((self.x - 1, self.y - 1), None)

    @property
    def adj(self) -> Tuple[BaseNode]:
        return filter(None, (self.up, self.left, self.down, self.right))

    @property
    def adj2(self) -> Tuple[BaseNode]:
        return filter(None, (self.up, self.left, self.down, self.right, self.leftUp, self.leftDown, self.rightUp, self.rightDown))
