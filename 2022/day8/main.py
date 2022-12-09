import sys
sys.path.append('../..')
import re
from collections import defaultdict
from map import Map, Node

USE_EXAMPLE = False
PRINT_DEBUG = False

LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def testVisible(tree, trees):
    good = True
    for x in trees:
        if x >= tree:
            good = False
            break
    return good
def getViewDistance(tree, trees):
    distance = 0
    for x in trees:
        distance += 1
        if x >= tree:
            break
    return distance

# Part 1
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    # map = Map.loadFromFile(file)
    map = []
    y = 0
    for line in file:
        map.append([])
        x = 0
        for v in line.strip():
            map[y].append(v)
            x += 1
        y += 1

    # print(map)
    visibleCount = 0
    for y in range(len(map)):
        if y == 0 or y == len(map) - 1:
            visibleCount += len(map[0])
            continue
        for x in range(len(map[0])):
            if x == 0 or x == len(map[0]) - 1:
                visibleCount += 1
                continue
            tree = int(map[y][x])
            left = [int(x) for x in map[y][:x]]
            right = [int(x) for x in map[y][x+1:]]
            up = [int(tx[x]) for tx in map[:y]]
            down = [int(tx[x]) for tx in map[y+1:]]

            l = testVisible(tree, reversed(left))
            r = testVisible(tree, right)
            u = testVisible(tree, reversed(up))
            d = testVisible(tree, down)

            if l or r or u or d:
                visibleCount += 1
    
    print(visibleCount)


# Part 2
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    map = []
    y = 0
    for line in file:
        map.append([])
        x = 0
        for v in line.strip():
            map[y].append(v)
            x += 1
        y += 1

    maxScenicScore = float('-inf')
    for y in range(len(map)):
        if y == 0 or y == len(map) - 1:
            continue
        for x in range(len(map[0])):
            if x == 0 or x == len(map[0]) - 1:
                continue
            tree = int(map[y][x])
            left = [int(x) for x in map[y][:x]]
            right = [int(x) for x in map[y][x+1:]]
            up = [int(tx[x]) for tx in map[:y]]
            down = [int(tx[x]) for tx in map[y+1:]]

            l = getViewDistance(tree, reversed(left))
            r = getViewDistance(tree, right)
            u = getViewDistance(tree, reversed(up))
            d = getViewDistance(tree, down)

            scenicScore = l * r * u * d
            if scenicScore > maxScenicScore:
                maxScenicScore = scenicScore
    
    print(maxScenicScore)
