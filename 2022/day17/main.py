import sys
sys.path.append('../..')
import re
from collections import defaultdict
from map import Map, Node, Unit

USE_EXAMPLE = False
PRINT_DEBUG = False

LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

class Rock:
    def __init__(self, shape: str, node: Node):
        self.node = node
        self.map = node.map
        self.shape = shape
        self.width = max([len(row) for row in shape.split('\n')])
        self.height = len(shape.split('\n'))
        self.units: list[Unit] = []
        for y, row in enumerate(reversed(shape.split('\n'))):
            # print(node.y - y)
            for x, rock in enumerate(row):
                if rock == '#':
                    self.units.append(Unit('@', node.map[node.x + x, node.y - y]))
        self.units.reverse()
        self.atRest = False
    def destroy(self):
        self.map.units = []
    def moveDown(self):
        hitSomething = False
        for unit in self.units:
            if unit.node.y == 0 or unit.node.downDefault.type == '#':
                hitSomething = True
            unit.node = unit.node.downDefault
        if hitSomething:
            for unit in self.units:
                unit.node = unit.node.upDefault
                unit.node.type = '#'
            self.atRest = True
        else:
            self.node = self.node.downDefault
    def moveRight(self):
        hitSomething = False
        for unit in self.units:
            if unit.node.x == 6 or unit.node.rightDefault.type == '#':
                hitSomething = True
            unit.node = unit.node.rightDefault
        if hitSomething:
            for unit in self.units:
                unit.node = unit.node.leftDefault
        else:
            self.node = self.node.rightDefault
    def moveLeft(self):
        hitSomething = False
        for unit in self.units:
            if unit.node.x == 0 or unit.node.leftDefault.type == '#':
                hitSomething = True
            unit.node = unit.node.leftDefault
        if hitSomething:
            for unit in self.units:
                unit.node = unit.node.rightDefault
        else:
            self.node = self.node.leftDefault

rock1 = '####'

rock2 = '.#.\n' +\
        '###\n' +\
        '.#.'

rock3 = '..#\n' +\
        '..#\n' +\
        '###'

rock4 = '#\n' +\
        '#\n' +\
        '#\n' +\
        '#'

rock5 = '##\n' +\
        '##'

rocks = [rock1, rock2, rock3, rock4, rock5]

instIdx = 0
def nextInstruction():
    global instIdx
    if instIdx >= len(instructions):
        instIdx = 0
    ret = instructions[instIdx]
    instIdx += 1
    return ret
rockIdx = 0
def nextRock(rocksFallen = None):
    if rocksFallen:
        return rocks[rocksFallen % 5]
    global rockIdx
    rockIdx %= len(rocks)
    # if rockIdx >= len(rocks):
    #     rockIdx = 0
    ret = rocks[rockIdx]
    rockIdx += 1
    return ret

def printMap(m: Map, msg: str, pause = True):
    print(msg)
    print(m)
    if pause:
        input(':>')


# Part 1
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]

    instructions = file.readline().strip()

    instIdx = 0
    rockIdx = 0

    m = Map()
    for x in range(-1, 8):
        for y in range(-4, 2, 1):
            if x == -1 or x == 7:
                Node(m, (x, y), '+' if y == 1 else '|')
            elif y == 1:
                Node(m, (x, y), '-')
            else:
                Node(m, (x, y), '.')
    
    highestRock = 1

    fallingRock = None
    for _ in range(2023):
        if fallingRock:
            highestRock = min(highestRock, fallingRock.node.y - fallingRock.height + 1)
            fallingRock.destroy()
        spawnNode = m[2, highestRock - 4]
        fallingRock = Rock(nextRock(), spawnNode)
        # printMap(m, 'SPAWN')
        while not fallingRock.atRest:
            # First, do wind
            inst = nextInstruction()
            if inst == '>':
                fallingRock.moveRight()
                pass
            elif inst == '<':
                fallingRock.moveLeft()
            # printMap(m, 'MOVE')
            # Then, fall
            fallingRock.moveDown()
            # printMap(m, 'FALL')
    # print(m)
    print(-highestRock+1)

# Part 2
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    instructions = file.readline().strip()

    instIdx = 0
    rockIdx = 0

    m = Map()
    for x in range(-1, 8):
        for y in range(-4, 2, 1):
            if x == -1 or x == 7:
                Node(m, (x, y), '+' if y == 1 else '|')
            elif y == 1:
                Node(m, (x, y), '-')
            else:
                Node(m, (x, y), '.')
    
    highestRock = 1

    ROCKS = set()
    REPEAT = {}

    fallingRock = None
    rocksFallen = 0
    TOTAL = 1000000000000
    skippedHeight = 0
    while rocksFallen < TOTAL:
        spawnNode = m[2, highestRock - 4]
        fallingRock = Rock(nextRock(rocksFallen), spawnNode)
        # printMap(m, 'SPAWN')
        while not fallingRock.atRest:
            # First, do wind
            inst = nextInstruction()
            if inst == '>':
                fallingRock.moveRight()
                pass
            elif inst == '<':
                fallingRock.moveLeft()
            # printMap(m, 'MOVE')
            # Then, fall
            fallingRock.moveDown()
            # printMap(m, 'FALL')
        ROCKS |= set([(u.node.x, u.node.y) for u in fallingRock.units])
        topRockFormation = frozenset([(x, -highestRock - -y) for x, y in ROCKS if -highestRock - -y <= 30])
        key = (instIdx, rocksFallen % 5, topRockFormation)
        miny = min([n.y for n in m.values() if n.type == '#'])
        if key in REPEAT:
            # print('in repeat:', key, key in REPEAT)
            # sys.exit()
            oldRocksFallen, oldHighestRock = REPEAT[key]
            cycleHeight = -miny - oldHighestRock
            # print(cycleHeight, -miny, oldHighestRock)
            cycleRockCount = rocksFallen - oldRocksFallen
            cyclesToSkip = (TOTAL - rocksFallen) // cycleRockCount
            skippedHeight += cyclesToSkip * cycleHeight
            rocksFallen += cyclesToSkip * cycleRockCount
        # print(rocksFallen, len(REPEAT), rockIdx)
        REPEAT[key] = (rocksFallen, -miny)
        rocksFallen += 1
        highestRock = min(highestRock, fallingRock.node.y - fallingRock.height + 1)
        fallingRock.destroy()

    print(-highestRock+1 + skippedHeight)
