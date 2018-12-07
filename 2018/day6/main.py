from collections import defaultdict

def distance(x, y, x2, y2):
    return abs(x - x2) + abs(y - y2)

def main():
    with open('input.txt', 'r') as f:
        grid = []
        for line in f:
            line = line.rstrip('\n')
            x, y = map(int, line.split(', '))
            grid.append((x, y))

        minX = 1e100
        minY = 1e100
        maxX = 0
        maxY = 0
        for x, y in grid:
            minX = min(minX, x)
            minY = min(minY, y)
            maxX = max(maxX, x)
            maxY = max(maxY, y)

        allPoints = []
        for x in range(minX, maxX + 1):
            for y in range(minY, maxY + 1):
                allPoints.append((x, y))

        distancesToPoints = defaultdict(dict)
        for x, y in allPoints:
            for x2, y2 in grid:
                distancesToPoints[(x, y)][(x2, y2)] = distance(x, y, x2, y2)

        # For part 2
        P2ANS = 0
        for (x, y), distances in distancesToPoints.items():
            s = sum([dist for xy, dist in distances.items()])
            if s < 10000:
                P2ANS += 1
        # end p2

        nearest = defaultdict(dict)
        for (x, y), distances in distancesToPoints.items():
            g = sorted(distances.items(), key=lambda kv: kv[1])
            shortest = g[0][1]
            nearest[(x, y)] = list(filter(lambda kv: kv[1] == shortest, g))

        owners = defaultdict(list)
        for (x, y), closest in nearest.items():
            if len(closest) > 1:
                continue

            owners[closest[0][0]].append((x, y))

        validOwners = defaultdict(list)
        for (x, y), owned in owners.items():
            invalid = False
            for x2, y2 in owned:
                if x2 == minX or x2 == maxX or y2 == minY or y2 == maxY:
                    invalid = True
                    break
            if not invalid:
                validOwners[(x, y)] = owned

        biggest = max(validOwners.items(), key=lambda kv: len(kv[1]))

        print('P1:', len(biggest[1]))
        print('P2:', P2ANS)

main()
