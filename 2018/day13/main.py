from collections import defaultdict, deque
from typing import List
import re

USE_EXAMPLE = False
PRINT_DEBUG = False

class Node:
    def __init__(self, map, x, y, type: str):
        self.map = map
        self.x = x
        self.y = y
        self.type = type

        self.map.setNode(x, y, self)

    def __str__(self):
        return '({}, {}): {}'.format(self.x, self.y, self.type)

class NodeImpl(Node):

    @property
    def up(self) -> Node:
        return self.map.getNode(self.x, self.y - 1)

    @property
    def down(self) -> Node:
        return self.map.getNode(self.x, self.y + 1)

    @property
    def left(self) -> Node:
        return self.map.getNode(self.x - 1, self.y)

    @property
    def right(self) -> Node:
        return self.map.getNode(self.x + 1, self.y)

class Cart:
    def __init__(self, facing: str, node: NodeImpl):
        self.facing = facing
        self.node = node
        self.turnState = deque(['left', 'straight', 'right'])

    def go(self):
        # Is intersection. Use turn deque
        if self.node.type == '+':
            toTurn = self.turnState[0]
            self.facing = self.getNewFacing(toTurn)

            self.forward()

            self.turnState.rotate(-1)

        elif self.node.type in '-|':
            self.forward()

        elif self.node.type == '/':
            if self.facing == '^':
                self.facing = '>'
            elif self.facing == '<':
                self.facing = 'v'
            elif self.facing == 'v':
                self.facing = '<'
            elif self.facing == '>':
                self.facing = '^'

            self.forward()

        elif self.node.type == '\\':
            if self.facing == '^':
                self.facing = '<'
            elif self.facing == '>':
                self.facing = 'v'
            elif self.facing == 'v':
                self.facing = '>'
            elif self.facing == '<':
                self.facing = '^'

            self.forward()

    def forward(self):
        if self.facing == '<':
            self.node = self.node.left
        elif self.facing == '>':
            self.node = self.node.right
        elif self.facing == '^':
            self.node = self.node.up
        elif self.facing == 'v':
            self.node = self.node.down

    def getNewFacing(self, turn):
        turnDeque = deque('<v>^')
        if turn == 'straight':
            return self.facing
        elif turn == 'left':
            while turnDeque[0] != self.facing:
                turnDeque.rotate(-1)
            turnDeque.rotate(-1)
            return turnDeque[0]
        elif turn == 'right':
            while turnDeque[0] != self.facing:
                turnDeque.rotate()
            turnDeque.rotate()
            return turnDeque[0]

class Map:
    def __init__(self, carts: List[Cart] = []):
        self.carts = []
        self.nodes = {}

    def getNode(self, x, y) -> Node:
        return self.nodes[(x, y)]

    def setNode(self, x, y, node: Node):
        self.nodes[(x, y)] = node

def genMap(f):
    cartMap = Map()

    y = 0
    for line in f:
        line = line.rstrip()
        x = 0
        for ch in line:
            node = NodeImpl(cartMap, x, y, ch)
            if ch in '><v^':
                if ch == '>':
                    node.type = '-'
                elif ch == '<':
                    node.type = '-'
                elif ch == '^':
                    node.type = '|'
                elif ch == 'v':
                    node.type = '|'
                cartMap.carts.append(Cart(ch, node))

            x += 1

        y += 1

    return cartMap

def part1():
    with open('example1.txt' if USE_EXAMPLE else 'input.txt', 'r') as f:
        cartMap = genMap(f)
        carts = cartMap.carts

        noCrash = True
        while noCrash:
            carts.sort(key=lambda c: [c.node.y, c.node.x])
            for cart in carts:
                cart.go()

                collision = defaultdict(list)
                for cart in carts:
                    collision[cart.node].append(cart)
                for node, cartL in list(collision.items()):
                    if len(cartL) < 2:
                        del collision[node]
                if len(collision) > 0:
                    collider = list(collision.items())[0]
                    noCrash = False
                    break

        if PRINT_DEBUG:
            print('0123456789'*15, end='')
            for (x, y), node in cartMap.nodes.items():
                if x == 0:
                    print()
                    print(y, end='')
                if node == collider[0]:
                    print('@', end='')
                    continue
                c = [cart for cart in carts if cart.node == node]
                if len(c) > 0:
                    print(c[0].facing, end='')
                else:
                    print(node.type, end='')

            print()
            print()

        return collider[0]


def part2():
    with open('example2.txt' if USE_EXAMPLE else 'input.txt', 'r') as f:
        cartMap = genMap(f)
        carts = cartMap.carts

        while len(carts) > 1:
            cartsToDelete = set()
            carts.sort(key=lambda c: [c.node.y, c.node.x])
            for cart in carts:
                if cart in cartsToDelete:
                    continue
                cart.go()

                collision = defaultdict(list)
                for cart in carts:
                    collision[cart.node].append(cart)
                for node, cartL in list(collision.items()):
                    if len(cartL) < 2:
                        del collision[node]
                if len(collision) > 0:
                    # They crashed! Delete them!
                    collisions = [i for sub in collision.values() for i in sub]
                    cartsToDelete = cartsToDelete.union(collisions)

            for ctd in cartsToDelete:
                carts.remove(ctd)

        return carts[0].node

print('P1:', part1())
print('P2:', part2())
