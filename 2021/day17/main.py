import sys
sys.path.append('../..')
import re
from collections import defaultdict
from map import Map, Node

USE_EXAMPLE = False
PRINT_DEBUG = False

class Probe:
    def __init__(self, xVel, yVel):
        self.x = self.y = 0
        self.xVel = xVel
        self.yVel = yVel

    def step(self):
        self.x += self.xVel
        self.y += self.yVel
        if self.xVel != 0:
            self.xVel += 1 if self.xVel < 0 else -1
        self.yVel -= 1

def sim(x1, x2, y1, y2, xVel, yVel):
    p = Probe(xVel, yVel)
    m = Map('.')
    if USE_EXAMPLE:
        Node(m, 0, 0, 'S')
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                Node(m, x, -y, 'T')
    highest = -float('inf')
    while p.x <= x2 and p.y >= y1:
        p.step()
        if USE_EXAMPLE:
            Node(m, p.x, -p.y, '#')
        if p.y > highest:
            highest = p.y
        if p.x >= x1 and p.x <= x2 and p.y >= y1 and p.y <= y2:
            return m, p, highest
    return None, None, None

with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    x1, x2, y1, y2 = map(int, re.match('target area: x=(-?\d+)\.\.(-?\d+), y=(-?\d+)\.\.(-?\d+)', file.readline()).groups())
    highest = -float('inf')
    s = set()
    for x in range(1, x2 + 1):
        for y in range(y1, -y1):
            m, p, h = sim(x1, x2, y1, y2, x, y)
            if m is None:
                continue
            if h > highest:
                highest = h
            s.add((x, y))
    # Part 1
    print(highest)
    # Part 2
    print(len(s))
