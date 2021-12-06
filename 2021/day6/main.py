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

# part 1
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

# part 2
# had to completely rethink how the data would be stored
# just kept track of the count of each fish by days left
fishMap = defaultdict(int)
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    for f in file.readline().strip().split(','):
        fishMap[int(f)] += 1
    for i in range(256):
        newFishMap = defaultdict(int)
        # all 0 day fish create new fish and return to 6 day
        for f, num in fishMap.items():
            # Move fish with days left to day-1
            newFishMap[f - 1] += num
        newFishMap[6] += newFishMap[-1]
        newFishMap[8] += newFishMap[-1]
        del newFishMap[-1]
        fishMap = newFishMap
    print(sum(fishMap.values()))
