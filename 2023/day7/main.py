import sys
sys.path.append('../..')
import re
from collections import defaultdict, deque, Counter
from map import Map, Node, Unit

USE_EXAMPLE = False
PRINT_DEBUG = False

LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

cardVals = '23456789TJQKA'
cardVals2 = 'J23456789TQKA'

def process(hand, jIsWild):
    cards = Counter(hand)

    if jIsWild and 'J' in cards:
        # Get most card
        target = cards.most_common(1)[0][0]
        if target == 'J' and len(cards.keys()) > 1:
            target = cards.most_common(2)[1][0]
        if target != 'J':
            cards[target] += cards['J']
            del cards['J']

    inv_map = defaultdict(list)
    for k, v in cards.items():
        inv_map[v] += [k]

    # print(inv_map)
    # print(sorted(cards.values()))
    isFive = bool(inv_map[5])
    isFour = bool(inv_map[4])
    isFullHouse = bool(inv_map[2] and inv_map[3])
    isThree = bool(inv_map[3])
    isTwoPair = len(inv_map[2]) == 2
    isOnePair = len(inv_map[2]) == 1
    if isFive:
        return 6
    elif isFour:
        return 5
    elif isFullHouse:
        return 4
    elif isThree:
        return 3
    elif isTwoPair:
        return 2
    elif isOnePair:
        return 1
    else:
        return 0

# Part 1
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]

    hands = []
    for line in file:
        line = line.strip()
        hand, bid = line.split()
        hands.append((hand, bid))
    hands = sorted(hands, key=lambda handbid: (process(handbid[0], False), [cardVals.index(card) for card in handbid[0]]))
    res = 0
    for rank, handbid in enumerate(hands, 1):
        res += rank * int(handbid[1])
    print(res)

# Part 2
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    # comma seperated values
    # vals = [int(x) for x in file.readline().strip().split(',')]
    hands = []
    for line in file:
        line = line.strip()
        hand, bid = line.split()
        hands.append((hand, bid))
    hands = sorted(hands, key=lambda handbid: (process(handbid[0], True), [cardVals2.index(card) for card in handbid[0]]))
    res = 0
    for rank, handbid in enumerate(hands, 1):
        res += rank * int(handbid[1])
    print(res)
