from collections import defaultdict, deque
from typing import Dict, Tuple, List

from map.node import Node
from map.unit import Unit as BaseUnit
from map.map import Map as BaseMap

WALL = '#'
FLOOR = '.'
GOBLIN = 'G'
ELF = 'E'

USE_EXAMPLE = False

class Map(BaseMap):
    def __str__(self):
        ret = ''
        for (x, _), node in self.items():
            if x == 0:
                ret += '\n'

            unitNodes = {u.node: u for u in self.units if u.alive}

            if node in unitNodes:
                ret += unitNodes[node].type
            else:
                ret += node.type

        return ret[1:]

class Unit(BaseUnit):
    def __init__(self, type: str, node: Node, map: Map, ap = 3):
        super().__init__(type, node, map)

        self.hp = 200
        self.ap = ap

    @property
    def ally(self):
        return not self.enemy

    @property
    def enemy(self):
        return GOBLIN if self.type == ELF else ELF

    @property
    def alive(self):
        return self.hp > 0

    def doTurn(self):
        sortedUnits = sorted([u for u in self.map.units if u.alive and u.type == self.enemy], key=lambda unit: [unit.node.y, unit.node.x])

        if len(sortedUnits) == 0:
            return True

        unitNodes = [u.node for u in self.map.units if u.alive]

        inRange = []
        for unit in sortedUnits:
            inRange.extend(filter(lambda adjNode: adjNode.type == FLOOR, unit.node.adj))

        inRange = set(inRange)

        if self.node in inRange:
            self.attack()
        else:

            nodesToCheck = deque([(self.node, 0)])
            pathMap = { self.node: (0, None) }
            beenTo = set()

            while nodesToCheck:
                node, dist = nodesToCheck.popleft()
                for adjNode in node.adj:
                    if adjNode.type == WALL or adjNode in unitNodes:
                        continue

                    # Check if this path was faster. Prioritize node ordering if dist is same
                    if adjNode not in pathMap or pathMap[adjNode] > (dist + 1, node):
                        pathMap[adjNode] = (dist + 1, node)

                    if adjNode in beenTo:
                        continue

                    if adjNode not in [c[0] for c in nodesToCheck]:
                        nodesToCheck.append((adjNode, dist + 1))

                beenTo.add(node)

            candidates = [(dist, node) for node, (dist, parent) in pathMap.items() if node in inRange and node not in unitNodes]
            distance, target = min(candidates, default=(None, None))
            if not target:
                return False

            while pathMap[target][0] > 1:
                target = pathMap[target][1]

            self.move(target)

            if self.node in inRange:
                self.attack()

        return False

    def move(self, target: Node):
        if target.type == FLOOR:
            self.node = target
        else:
            raise Exception("Node is unavailable!")

    def attack(self):
        enemies = filter(lambda u: u.alive and u.type == self.enemy, self.map.units)
        adjEnemies = filter(lambda e: e.node in self.node.adj, enemies)
        target = sorted(adjEnemies, key=lambda e: (e.hp, e.node))[0]

        target.hp -= self.ap

with open('example2.txt' if USE_EXAMPLE else 'input.txt', 'r') as f:
    y = 0
    cave = Map()
    for line in f:
        for x, ch in enumerate(line.strip()):
            node = Node(cave, x, y, ch)
            if ch == GOBLIN or ch == ELF:
                node.type = '.'
                cave.units.append(Unit(ch, cave[(x, y)], cave))
        y += 1

    round = 0
    end = False
    while not end:

        sortedUnits = sorted(cave.units, key=lambda unit: unit.node)

        for unit in sortedUnits:
            if unit.alive and unit.doTurn():
                end = True
                break

        if end:
            break

        round += 1

    print('P1:', round * sum([unit.hp for unit in cave.units if unit.alive]))

elvesWinNoDeath = True
AP = 3
while elvesWinNoDeath:
    with open('example2.txt' if USE_EXAMPLE else 'input.txt', 'r') as f:
        y = 0
        cave = Map()
        for line in f:
            for x, ch in enumerate(line.strip()):
                node = Node(cave, x, y, ch)
                if ch == GOBLIN or ch == ELF:
                    node.type = '.'
                    cave.units.append(Unit(ch, cave[(x, y)], cave, AP if ch == ELF else 3))
            y += 1

        initialElfCount = len([unit for unit in cave.units if unit.type == ELF])

        round = 0
        end = False
        while not end:

            sortedUnits = sorted(cave.units, key=lambda unit: unit.node)

            for unit in sortedUnits:
                if unit.alive and unit.doTurn():
                    end = True
                    break

            if end:
                break

            round += 1

        elfCount = len([unit for unit in cave.units if unit.type == ELF and unit.alive])
        if elfCount == initialElfCount:
            elvesWinNoDeath = False
        else:
            AP += 1

print('P2:', round * sum([unit.hp for unit in cave.units if unit.alive]))

# print(Map().units)
# print(Map().units)
# m = Map()
# m.units.append(Unit('E', node, m))
# print(m.units)
