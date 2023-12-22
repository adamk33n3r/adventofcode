import sys
sys.path.append('../..')
import re
from collections import defaultdict, deque
from map import Map, Node, Unit

USE_EXAMPLE = False
PRINT_DEBUG = False

LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def playGame(sets):
    bags = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }
    for set in sets:
        for pull in set:
            num, color = pull.split(' ')
            if int(num) > bags[color]:
                return False
    return True
def playGame2(sets):
    mins = {
        'red': 0,
        'green': 0,
        'blue': 0,
    }
    for set in sets:
        for pull in set:
            num, color = pull.split(' ')
            num = int(num)
            if num > mins[color]:
                mins[color] = num
    return mins

# Part 1
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    acc = 0
    for line in file:
        line = line.strip()
        game, setsLine = line.split(': ')
        sets = setsLine.split('; ')
        sets = [set.split(', ') for set in sets]
        possible = playGame(sets)
        if possible:
            gameId = game.split(' ')[1]
            acc += int(gameId)
    print(acc)


# Part 2
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    acc = 0
    for line in file:
        line = line.strip()
        game, setsLine = line.split(': ')
        sets = setsLine.split('; ')
        sets = [set.split(', ') for set in sets]
        mins = playGame2(sets)
        acc += mins['red'] * mins['green'] * mins['blue']
    print(acc)
