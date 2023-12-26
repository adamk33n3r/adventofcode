import sys
sys.path.append('../..')
import re
from collections import defaultdict, deque
from map import Map, Node, Unit

USE_EXAMPLE = False
PRINT_DEBUG = False

LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
def calcDistance(chargeTime: int, totalTime: int) -> int:
    totalTime -= chargeTime
    return totalTime * chargeTime

def solve(timeVals, distanceVals):
    res = 1
    for time, distToBeat in zip(timeVals, distanceVals):
        first = None
        for i in range(time+1):
            dist = calcDistance(i, time)
            if first is None and dist > distToBeat:
                first = i
                break
        res *= int(((time/2) - first)*2+1)
    return res

# Part 1
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    timeVals = [int(x) for x in file.readline().split(':')[1].split()]
    distanceVals = [int(x) for x in file.readline().split(':')[1].split()]
    print(solve(timeVals, distanceVals))

# Part 2
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    timeVals = int(file.readline().split(':')[1].replace(' ', ''))
    distanceVals = int(file.readline().split(':')[1].replace(' ', ''))
    print(solve([timeVals], [distanceVals]))
