import sys
sys.path.append('../..')
import re
from collections import defaultdict, deque
from map import Map, Node, Unit

USE_EXAMPLE = False
PRINT_DEBUG = False

LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def getnum(n: Node, visited: set):
    return getnumhelper(n, visited)
def getnumhelper(n: Node, visited: set):
    if n in visited:
        return ''
    visited.add(n)
    s = n.type
    if n.left is not None and n.left.type.isdigit():
        s = getnumhelper(n.left, visited) + s
    if n.right is not None and n.right.type.isdigit():
        s = s + getnumhelper(n.right, visited)
    return s

# Part 1
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    m = Map.loadFromFile(file)

    visited = set()
    partnums = []
    for y in range(m.height):
        for x in range(m.width):
            n = m[x, y]
            if n.type.isdigit():
                pass
            elif n.type == '.':
                pass
            else:
                for adj in n.adj2:
                    if adj not in visited and adj.type.isdigit():
                        partnums.append(getnum(adj, visited))
    print(sum([int(p) for p in partnums]))

# Part 2
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    m = Map.loadFromFile(file)

    visited = set()
    ratios = 0
    for y in range(m.height):
        for x in range(m.width):
            n = m[x, y]
            if n.type == '*':
                nums = []
                for adj in n.adj2:
                    if adj not in visited and adj.type.isdigit():
                        nums.append(getnum(adj, visited))
                if len(nums) == 2:
                    ratio = int(nums[0]) * int(nums[1])
                    ratios += ratio
    print(ratios)
