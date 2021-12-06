import re
from itertools import zip_longest
from collections import defaultdict

USE_EXAMPLE = False
PRINT_DEBUG = False

fish = []
newFish = []

class Fish:
    daysToProduce = 8
    def __init__(self, start = 8):
        self.daysToProduce = start
    def tick(self):
        self.daysToProduce -= 1
        if self.daysToProduce < 0:
            self.daysToProduce = 6
            # spawn new fish
            newFish.append(Fish())

with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    for f in file.readline().strip().split(','):
        fish.append(Fish(int(f)))
    for i in range(80):
        for f in fish:
            f.tick()
        for nf in newFish:
            fish.append(nf)
        newFish = []
    print(len(fish))
