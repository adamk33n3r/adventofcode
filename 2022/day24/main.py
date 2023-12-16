import sys
sys.path.append('../..')
import re
from collections import defaultdict, deque
from map import Map, Node, Unit
from typing import Tuple
from dataclasses import dataclass

USE_EXAMPLE = False
PRINT_DEBUG = False

LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

class Expedition(Unit):
    def __init__(self, node: Node):
        super().__init__('#', node)

@dataclass(frozen=True)
class Pos:
    pos: Tuple[int, int]

    @property
    def x(self):
        return self.pos[0]
    @property
    def y(self):
        return self.pos[1]
    @property
    def right(self):
        return Pos((self.x + 1, self.y))
    @property
    def left(self):
        return Pos((self.x - 1, self.y))
    @property
    def up(self):
        return Pos((self.x, self.y - 1))
    @property
    def down(self):
        return Pos((self.x, self.y + 1))

@dataclass(frozen=True)
class Blizzard(Pos):
    dir: str

    def moveAhead(self, map):
        newPos = self.pos
        if self.dir == '>':
            if map[self.right.pos].type == WALL:
                newPos = (1, self.pos[1])
            else:
                newPos = self.right.pos
        elif self.dir == '<':
            if map[self.left.pos].type == WALL:
                newPos = (map.maxX - 1, self.pos[1])
            else:
                newPos = self.left.pos
        elif self.dir == '^':
            if map[self.up.pos].type == WALL:
                newPos = (self.pos[0], map.maxY - 1)
            else:
                newPos = self.up.pos
        elif self.dir == 'v':
            if map[self.down.pos].type == WALL:
                newPos = (self.pos[0], 1)
            else:
                newPos = self.down.pos
        else:
            assert False, self.dir
        return Blizzard(newPos, self.dir)

def traverse(START: Pos, END: Pos, blizzardPositions, startT: int = 0):
    processQueue: deque[Tuple[Pos, frozenset[Blizzard], int]] = deque([( START, blizzardPositions[startT%len(blizzardPositions)], startT, [] )])
    SEEN = set()
    while processQueue:
        pos, blizzardPosSet, t, path = processQueue.popleft()
        if not (0 <= pos.x <= m.maxX and 0 <= pos.y <= m.maxY and m[pos.pos].type != '#'):
            continue

        if pos == END:
            return (t, path)


        if (pos, blizzardPosSet, t) in SEEN:
            continue
        SEEN.add((pos, blizzardPosSet, t))

        blizzardPosSet = blizzardPositions[(t+1)%len(blizzardPositions)]

        # print('===========')
        if pos.right.pos not in blizzardPosSet:
            # print('right')
            processQueue.append((pos.right, blizzardPosSet, t+1, path+[pos.pos]))
        if pos.left.pos not in blizzardPosSet:
            # print('left')
            processQueue.append((pos.left, blizzardPosSet, t+1, path+[pos.pos]))
        if pos.up.pos not in blizzardPosSet:
            # print('up')
            processQueue.append((pos.up, blizzardPosSet, t+1, path+[pos.pos]))
        if pos.down.pos not in blizzardPosSet:
            # print('down')
            processQueue.append((pos.down, blizzardPosSet, t+1, path+[pos.pos]))
        # wait
        if pos.pos not in blizzardPosSet:
            # print('wait')
            processQueue.append((pos, blizzardPosSet, t+1, path+[pos.pos]))

# Part 1
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    m = Map()
    START: Pos = None
    END: Pos = None
    for y, line in enumerate(file):
        for x, c in enumerate(line.strip()):
            if c == '.' or c == '#':
                n = Node(m, (x, y), c)
                if START is None and y == 0 and n.type == '.':
                    START = Pos((n.x, n.y))
            else:
                Unit(c, Node(m, (x, y), '.'))
    for x in range(m.minX, m.maxX + 1):
        n = m[x, m.maxY]
        if n.type == '.':
            END = Pos((n.x, n.y))
            break


    WALL = '#'
    blizzards = m.units
    # print(START, END)

    blizzardPosSet = frozenset([Blizzard(u.node.pos[:2], u.type) for u in blizzards])
    t = 0
    blizzardPositions = {
        t: frozenset([b.pos for b in blizzardPosSet])
    }
    firstBlizzardLayout = blizzardPosSet
    while True:
        t += 1
        blizzardPosSet = frozenset([blizzard.moveAhead(m) for blizzard in blizzardPosSet])
        fs = frozenset([b.pos for b in blizzardPosSet])
        # Will now repeat
        if blizzardPosSet == firstBlizzardLayout:
            # print(t, blizzardPosSet)
            break
        blizzardPositions[t] = fs
    # print('blizzard cycle repeats every:', t, len(blizzardPositions))

    t, path = traverse(START, END, blizzardPositions)
    print('p1:', t)
    t2, path = traverse(END, START, blizzardPositions, t)
    t3, path = traverse(START, END, blizzardPositions, t2)
    print('p2:', t3)


