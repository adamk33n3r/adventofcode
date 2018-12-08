from collections import defaultdict
import re

USE_EXAMPLE = False
PRINT_DEBUG = False

class Node:
    def __init__(self, children, metadata):
        self.children = children
        self.metadata = metadata

    def getValue(self):
        if len(self.children) == 0:
            return sum(self.metadata)

        return sum([
            self.children[childIdx].getValue()
            for childIdx in map(lambda x: x - 1, self.metadata)
                if childIdx < len(self.children)
        ])

with open('example.txt' if USE_EXAMPLE else 'input.txt', 'r') as f:
    digits = f.readline().rstrip().split()

    it = iter(digits)

    meta = []

    def getMeta(it):
        numChildren = int(next(it))
        numMeta = int(next(it))

        for _ in range(numChildren):
            getMeta(it)

        for _ in range(numMeta):
            meta.append(int(next(it)))

    getMeta(it)

    print('P1:', sum(meta))

    it = iter(digits)

    def part2(it):
        numChildren = int(next(it))
        numMeta = int(next(it))

        children = [part2(it) for _ in range(numChildren)]
        meta = [int(next(it)) for _ in range(numMeta)]

        return Node(children, meta)

    print('P2:', part2(it).getValue())

