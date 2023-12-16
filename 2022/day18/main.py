import sys
sys.path.append('../..')
import re
from collections import defaultdict, deque
from map import Map, Node

USE_EXAMPLE = False
PRINT_DEBUG = False

LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Part 1
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    C = []
    for line in file:
        line = line.strip()
        x, y, z = map(int, line.split(','))
        C.append((x,y,z))
    sides = 0
    tot = len(C) * 6
    for x,y,z in C:
        for ox,oy,oz in C:
            if x == ox and y == oy:
                if abs(z - oz) == 1:
                    sides += 1
            elif x == ox and z == oz:
                if abs(y - oy) == 1:
                    sides += 1
            elif y == oy and z == oz:
                if abs(x - ox) == 1:
                    sides += 1
    print(tot - sides)
        

# Part 2
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]

    # Map coming in clutch this time for adjZ
    m = Map()
    C = []
    for line in file:
        line = line.strip()
        x, y, z = map(int, line.split(','))
        C.append((x,y,z))
        Node(m, (x, y, z), '#')
    sides = 0
    external = set()
    internal = set()
    def isExternal(node: Node):
        # memoize stuffs
        if node in external:
            return True
        if node in internal:
            return False

        # Walk around
        visited = set()
        process = deque([ node ])
        while process:
            node = process.popleft()
            # Skip if we've already visited it
            # Or if it's a point in our input (a block)
            if node in visited or node.type == '#':
                continue
            visited.add(node)

            # If we've visited this many nodes, we're probably external
            # There must be a big freaking hole inside for it to need this
            # many to visit. Trial and error shows that 1373 is the lowest
            # that works for my input. That's a big hole.
            if len(visited) > 1373:
                # memoize external nodes
                for node in visited:
                    external.add(node)
                return True
            for adj in node.adjZDefault:
                process.append(adj)

        # memoize internal nodes
        for node in visited:
            internal.add(node)
        return False

    for x,y,z in C:
        # Check all faces
        for dx,dy,dz in [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]:
            if isExternal(m[x+dx, y+dy, z+dz]):
                sides += 1
    print(sides)

