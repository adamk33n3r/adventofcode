import sys
sys.path.append('../..')
import re
from collections import defaultdict, deque
from map import Map, Node, Unit
from itertools import cycle

USE_EXAMPLE = False
PRINT_DEBUG = False

LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

class Elf(Unit):
    def __init__(self, node: Node, idx: int):
        super().__init__('#', node)
        self.idx = idx

    def proposeMove(self, unitNodes, _decisionList):
        noAdj = True
        for adj in self.node.adj2Default:
            if adj in unitNodes:
                noAdj = False
                break

        if noAdj:
            # next(_decisionList)
            return None

        decision = None
        for i in range(4):
            nextFn = _decisionList[i]
            # nextFn = next(_decisionList)
            if decision:
                continue
            res = nextFn(self.node, unitNodes)
            if res:
                decision = res
        # skip for next time
        # next(self._decisionList)
        return decision

def _checkNorth(node, unitNodes):
    if node.upDefault not in unitNodes and node.leftUpDefault not in unitNodes and node.rightUpDefault not in unitNodes:
    # if not (self.map.unitAt(node.upDefault) or self.map.unitAt(node.leftUpDefault) or self.map.unitAt(node.rightUpDefault)):
        return node.upDefault
    return None
def _checkSouth(node, unitNodes):
    if node.downDefault not in unitNodes and node.leftDownDefault not in unitNodes and node.rightDownDefault not in unitNodes:
    # if not (self.map.unitAt(node.downDefault) or self.map.unitAt(node.leftDownDefault) or self.map.unitAt(node.rightDownDefault)):
        return node.downDefault
    return None
def _checkWest(node, unitNodes):
    if node.leftDefault not in unitNodes and node.leftDownDefault not in unitNodes and node.leftUpDefault not in unitNodes:
    # if not (self.map.unitAt(node.leftDefault) or self.map.unitAt(node.leftDownDefault) or self.map.unitAt(node.leftUpDefault)):
        return node.leftDefault
    return None
def _checkEast(node, unitNodes):
    if node.rightDefault not in unitNodes and node.rightDownDefault not in unitNodes and node.rightUpDefault not in unitNodes:
    # if not (self.map.unitAt(node.rightDefault) or self.map.unitAt(node.rightDownDefault) or self.map.unitAt(node.rightUpDefault)):
        return node.rightDefault
    return None

decisionList = ([
    _checkNorth,
    _checkSouth,
    _checkWest,
    _checkEast,
])

# Part 1
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    m = Map()
    elves: list[Elf] = []
    i = 0
    for y, line in enumerate(file):
        for x, c in enumerate(line):
            n = Node(m, (x, y), '.')
            if c == '#':
                elves.append(Elf(n, i))
                i += 1

    # print('== Initial State ==')
    # print(m)
    # input(':> ')

    round = 1
    lastNodes = set()
    while True:
        proposedMoves: dict[Node, list[Elf]] = defaultdict(list)
        unitNodes = [unit.node for unit in m.units]
        for i, elf in enumerate(elves):
            move = elf.proposeMove(unitNodes, decisionList)
            # print('Elf', i, 'at', elf.node, 'proposes to move to', move)
            if move is None:
                continue
            proposedMoves[move].append(elf)
        # skip for next time
        # next(decisionList)
        decisionList = decisionList[1:] + [decisionList[0]]

        anyMoved = False
        # for move, elf in [(move, elves[0]) for move, elves in proposedMoves.items() if len(elves) == 1]:
        #     elf.node = move
        #     anyMoved = True
        for move, elvesProposed in proposedMoves.items():
            if len(elvesProposed) == 1:
                elvesProposed[0].node = move
                anyMoved = True
        # for i, elf in enumerate(elves):
        #     print(i, elf.node)
        print('End of Round', round)

        # thisNodes = set([u.node for u in m.units])
        # if thisNodes == lastNodes:
        if not anyMoved:
            print('Part 2:', round)
            break

        if round == 10:
            m.trim()
            print('Part 1:', ((m.maxX - m.minX + 1) * (m.maxY - m.minY + 1)) - len(elves))
        round += 1
