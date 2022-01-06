import sys
sys.path.append('../..')
import re
from collections import defaultdict
from map import Map, Node

USE_EXAMPLE = False
PRINT_DEBUG = False

class Board:
    def __init__(self, p1, p2) -> None:
        self.p1 = p1
        self.p2 = p2
    def movep1(self, amt):
        self.p1 += amt
        while self.p1 > 10:
            self.p1 -= 10
    def movep2(self, amt):
        self.p2 += amt
        while self.p2 > 10:
            self.p2 -= 10

class Die100:
    def __init__(self) -> None:
        self.pos = 0
        self.count = 0
    def roll(self):
        self.count += 1
        self.pos += 1
        if self.pos > 100:
            self.pos = 1
        return self.pos

# Part 1
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    p1 = int(file.readline().strip()[-1])
    p2 = int(file.readline().strip()[-1])
    scores = [0,0]
    b = Board(p1, p2)

    d = Die100()

    win = None
    while True:
        diceRoll = d.roll() + d.roll() + d.roll()
        b.movep1(diceRoll)
        scores[0] += b.p1

        if scores[0] >= 1000:
            win = 'p1'
            break

        diceRoll = d.roll() + d.roll() + d.roll()
        b.movep2(diceRoll)
        scores[1] += b.p2

        if scores[1] >= 1000:
            win = 'p2'
            break

    # print(win + ' wins with ' + str(scores[0] if win == 'p1' else scores[1]))
    if win == 'p1':
        print(scores[1] * d.count)
    else:
        print(scores[0] * d.count)


winnings = {}

def takeTurn(p1, p2, s1, s2):
    if s1 >= 21:
        return (1, 0)
    if s2 >= 21:
        return (0, 1)
    if (p1, p2, s1, s2) in winnings:
        return winnings[(p1,p2,s1,s2)]
    res = (0, 0)
    for roll1 in [1,2,3]:
        for roll2 in [1,2,3]:
            for roll3 in [1,2,3]:
                p1mod = p1+roll1+roll2+roll3
                while p1mod > 10:
                    p1mod -= 10
                s1mod = s1+p1mod
                r1, r2 = takeTurn(p2, p1mod, s2, s1mod)
                res = (res[0]+r2, res[1]+r1)
    winnings[(p1,p2,s1,s2)] = res
    return res

# Part 2
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    p1 = int(file.readline().strip()[-1])
    p2 = int(file.readline().strip()[-1])

    results = takeTurn(p1, p2, 0, 0)
    print(max(results))
