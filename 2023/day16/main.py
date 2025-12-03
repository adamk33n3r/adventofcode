import sys
sys.path.append('../..')
import re
from collections import defaultdict, deque
from map import Map, Node, Unit

USE_EXAMPLE = False
PRINT_DEBUG = False

LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

class Beam(Unit):
    def __init__(self, node: Node, dir: str):
        super().__init__('*', node)
        self.dir = dir

    def tick(self):
        newBeam = None
        if self.node.type == '.':
            pass
        elif self.node.type == '|':
            if self.dir == 'r' or self.dir == 'l':
                newBeam = Beam(self.node, 'u')
                self.dir = 'd'
        elif self.node.type == '-':
            if self.dir == 'u' or self.dir == 'd':
                newBeam = Beam(self.node, 'l')
                self.dir = 'r'
        elif self.node.type == '\\':
            if self.dir == 'r': self.dir = 'd'
            elif self.dir == 'd': self.dir = 'r'
            elif self.dir == 'l': self.dir = 'u'
            elif self.dir == 'u': self.dir = 'l'
        elif self.node.type == '/':
            if self.dir == 'r': self.dir = 'u'
            elif self.dir == 'd': self.dir = 'l'
            elif self.dir == 'l': self.dir = 'd'
            elif self.dir == 'u': self.dir = 'r'

        self.node = self._getForward()
        return newBeam

    def _getForward(self) -> Node:
        if self.dir == 'u': return self.node.up
        if self.dir == 'r': return self.node.right
        if self.dir == 'd': return self.node.down
        if self.dir == 'l': return self.node.left

def solve(startPos, startDir, m, e):
    w, h = m.width, m.height
    def inBounds(beam: Beam) -> bool:
        if beam.node is None: return False
        return 0 <= beam.node.x < w and 0 <= beam.node.y < h

    beam = Beam(m[startPos], startDir)
    e[startPos[0], startPos[1], 0].type = '#'
    seen = set()
    while m.units:
        for beam in m.units:
            if (beam.node.pos, beam.dir) in seen:
                m.units.remove(beam)
                continue
            seen.add((beam.node.pos, beam.dir))
            newBeam = beam.tick()
            if newBeam and inBounds(newBeam):
                e[newBeam.node.x, newBeam.node.y, 0].type = '#'
            if not inBounds(beam):
                m.units.remove(beam)
                continue
            e[beam.node.x, beam.node.y, 0].type = '#'
    # print(e)
    count = len([n for n in e.values() if n.type == '#'])
    return count

# Part 1
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma separated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    m = Map.loadFromFile(file)
    e = Map()

    ans = solve((0,0), 'r', m, e)
    print(ans)


# Part 2
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma separated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    m = Map.loadFromFile(file)
    e = Map()

    ans = 0
    w, h = m.width, m.height
    for y in range(h):
        ans = max(ans, solve((0,y), 'r', m, Map()))
        ans = max(ans, solve((w-1,y), 'l', m, Map()))
    for x in range(w):
        ans = max(ans, solve((x,0), 'd', m, Map()))
        ans = max(ans, solve((x,h-1), 'u', m, Map()))
    print(ans)
