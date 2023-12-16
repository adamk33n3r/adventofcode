from typing import Tuple, Union, Optional

class BaseNode:
    def __init__(self, map, pos: Tuple[int, int, Optional[int]], value: str):
        self.map = map
        if len(pos) < 3:
            pos += (0,)
        self.x, self.y, self.z = pos
        self.type = value

        # print(len(self.map.items()))
        self.map[(self.x, self.y, self.z)] = self
        # print(len(self.map.items()))

    @property
    def pos(self):
        return (self.x, self.y, self.z)

    def __str__(self):
        return '({}, {}, {}): {}'.format(self.x, self.y, self.z, self.type)

    def __gt__(self, other):
        return (self.z, self.y, self.x) > (other.z, other.y, other.x)

    def __lt__(self, other):
        return (self.z, self.y, self.x) < (other.z, other.y, other.x)

class Node(BaseNode):

    @property
    def up(self) -> BaseNode:
        return self.map.get((self.x, self.y - 1, self.z), None)

    @property
    def down(self) -> BaseNode:
        return self.map.get((self.x, self.y + 1, self.z), None)

    @property
    def left(self) -> BaseNode:
        return self.map.get((self.x - 1, self.y, self.z), None)

    @property
    def right(self) -> BaseNode:
        return self.map.get((self.x + 1, self.y, self.z), None)

    @property
    def rightDown(self) -> BaseNode:
        return self.map.get((self.x + 1, self.y + 1, self.z), None)

    @property
    def rightUp(self) -> BaseNode:
        return self.map.get((self.x + 1, self.y - 1, self.z), None)

    @property
    def leftDown(self) -> BaseNode:
        return self.map.get((self.x - 1, self.y + 1, self.z), None)

    @property
    def leftUp(self) -> BaseNode:
        return self.map.get((self.x - 1, self.y - 1, self.z), None)

    @property
    def upDefault(self) -> BaseNode:
        return self.map[self.x, self.y - 1, self.z]

    @property
    def downDefault(self) -> BaseNode:
        return self.map[self.x, self.y + 1, self.z]

    @property
    def leftDefault(self) -> BaseNode:
        return self.map[self.x - 1, self.y, self.z]

    @property
    def rightDefault(self) -> BaseNode:
        return self.map[self.x + 1, self.y, self.z]

    @property
    def rightDownDefault(self) -> BaseNode:
        return self.map[self.x + 1, self.y + 1, self.z]

    @property
    def rightUpDefault(self) -> BaseNode:
        return self.map[self.x + 1, self.y - 1, self.z]

    @property
    def leftDownDefault(self) -> BaseNode:
        return self.map[self.x - 1, self.y + 1, self.z]

    @property
    def leftUpDefault(self) -> BaseNode:
        return self.map[self.x - 1, self.y - 1, self.z]

    @property
    def front(self) -> BaseNode:
        return self.map.get((self.x, self.y, self.z - 1), None)

    @property
    def frontDefault(self) -> BaseNode:
        return self.map[self.x, self.y, self.z - 1]

    @property
    def back(self) -> BaseNode:
        return self.map.get((self.x, self.y, self.z + 1), None)

    @property
    def backDefault(self) -> BaseNode:
        return self.map[self.x, self.y, self.z + 1]



    @property
    def adj(self) -> Tuple[BaseNode]:
        return filter(None, (self.up, self.left, self.down, self.right))

    @property
    def adjDefault(self) -> Tuple[BaseNode]:
        return (self.upDefault, self.leftDefault, self.downDefault, self.rightDefault)

    @property
    def adj2(self) -> Tuple[BaseNode]:
        return filter(None, (self.up, self.left, self.down, self.right, self.leftUp, self.leftDown, self.rightUp, self.rightDown))

    @property
    def adj2Default(self) -> Tuple[BaseNode]:
        return (self.upDefault, self.leftDefault, self.downDefault, self.rightDefault, self.leftUpDefault, self.leftDownDefault, self.rightUpDefault, self.rightDownDefault)

    @property
    def surround(self) -> Tuple[BaseNode]:
        return filter(None, (self.leftUp, self.up, self.rightUp, self.left, self, self.right, self.leftDown, self.down, self.rightDown))

    @property
    def diag(self) -> Tuple[BaseNode]:
        return filter(None, (self.leftUp, self.rightUp, self.rightDown, self.leftDown))

    @property
    def diagDefault(self) -> Tuple[BaseNode]:
        return (self.leftUpDefault, self.rightUpDefault, self.rightDownDefault, self.leftDownDefault)

    @property
    def adjZ(self) -> Tuple[BaseNode]:
        return filter(None, (self.up, self.left, self.down, self.right, self.back, self.front))

    @property
    def adjZDefault(self) -> Tuple[BaseNode]:
        return (self.upDefault, self.leftDefault, self.downDefault, self.rightDefault, self.backDefault, self.frontDefault)
