import sys
sys.path.append('../..')
import re
from collections import defaultdict, deque
from map import Map, Node, Unit

USE_EXAMPLE = False
PRINT_DEBUG = False

LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Part 1
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    acc = 0
    for line in file:
        line = line.strip()
        card, numbers = line.split(': ')
        _, cardNum = card.split()
        winning, yours = [[int(x) for x in n] for n in [n.split() for n in numbers.split(' | ')]]
        cardVal = 0
        for win in winning:
            if win in yours:
                if cardVal == 0:
                    cardVal = 1
                else:
                    cardVal *= 2
        acc += cardVal
    print(acc)

# Part 2
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    cards = defaultdict(int)
    for line in file:
        line = line.strip()
        card, numbers = line.split(': ')
        _, cardNum = card.split()
        cardNum = int(cardNum)
        winning, yours = [[int(x) for x in n] for n in [n.split() for n in numbers.split(' | ')]]
        s = sum([win in yours for win in winning])
        dupes = cards[cardNum]
        cards[cardNum] += 1 # count original
        for time in range(dupes + 1):
            for i in range(s):
                cards[cardNum + i + 1] += 1
    print(sum(cards.values()))
