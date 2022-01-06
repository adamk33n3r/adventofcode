import sys
sys.path.append('../..')
import re
from collections import defaultdict
from map import Map, Node

USE_EXAMPLE = False
PRINT_DEBUG = False

# Part 1
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    m = Map()
    l=0
    for line in file:
        state,xp,yp,zp = re.match('(\w+) x=(-?\d+\.\.-?\d+),y=(-?\d+\.\.-?\d+),z=(-?\d+\.\.-?\d+)', line.strip()).groups()
        x1, x2 = map(int, xp.split('..'))
        y1, y2 = map(int, yp.split('..'))
        z1, z2 = map(int, zp.split('..'))
        # print(state, x1, x2, y1, y2, z1, z2)
        # if any([i < -50 or i > 50 for i in [x1,x2,y1,y2,z1,z2]]):
        #     continue
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                for z in range(z1, z2 + 1):
                    m[(x, y, z)].type = '.' if state == 'off' else '#'
        # print(m.minX, m.maxX, m.minY, m.maxY, m.minZ, m.maxZ)
        l += 1
        print(l)
    print(sum([1 if n.type == '#' else 0 for n in m.values()]))

# Part 2
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    for line in file:
        line = line.strip()
