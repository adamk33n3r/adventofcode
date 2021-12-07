import math

USE_EXAMPLE = False
PRINT_DEBUG = False

with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    positions = [int(x) for x in file.readline().strip().split(',')]
    minx = min(positions)
    maxx = max(positions)
    chosen = None
    chosenFuel = math.inf
    for i in range(minx, maxx):
        totalFuel = 0
        for pos in positions:
            dist = abs(pos - i)
            totalFuel += dist
        if totalFuel < chosenFuel:
            chosenFuel = totalFuel
            chosen = i
    print(chosenFuel)

with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    positions = [int(x) for x in file.readline().strip().split(',')]
    minx = min(positions)
    maxx = max(positions)
    chosen = None
    chosenFuel = math.inf
    for i in range(minx, maxx):
        totalFuel = 0
        for pos in positions:
            dist = abs(pos - i)
            # This is what I used to solve it, but it takes like 30s-1m to run
            # The formula below is way faster
            # for d in range(1, dist + 1):
            #     newDist += d
            newDist = dist * (dist + 1) // 2
            totalFuel += newDist
        if totalFuel < chosenFuel:
            chosenFuel = totalFuel
            chosen = i
    print(chosenFuel)
