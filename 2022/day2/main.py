import sys
sys.path.append('../..')
import re
from collections import defaultdict
from map import Map, Node

USE_EXAMPLE = False
PRINT_DEBUG = False

scores = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3,
}

def play(opp, me):
    if scores[opp] == scores[me]:
        return 3
    if scores[opp] - scores[me] == 1 or scores[opp] - scores[me] == -2:
        return 0
    else:
        return 6


# Part 1
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    total = 0
    for line in file:
        opp, me = line.strip().split()
        res = play(opp, me)

        if PRINT_DEBUG:
            print(opp, me, res, scores[me], res + scores[me])
        total += res + scores[me]
    print(total)

moves = [ 'A', 'B', 'C' ]

# x lose, y draw, z win
def getMove(opp, end):
    if end == 'X':
        return moves[moves.index(opp) - 1]
    elif end == 'Y':
        return moves[moves.index(opp)]
    elif end == 'Z':
        return moves[(moves.index(opp) + 1) % len(moves)]

# Part 2
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    total = 0
    for line in file:
        opp, end = line.strip().split()
        me = getMove(opp, end)
        res = play(opp, me)

        if PRINT_DEBUG:
            print(opp, me, res, scores[me], res + scores[me])
        total += res + scores[me]
    print(total)
