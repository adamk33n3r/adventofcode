# Day 8

We had a 2d grid today with tree heights at each coordinate. I parsed in the input as a 2d list. I was originally going to use my Map module but it didn't support getting slices of rows/cols which I knew I would want.

The goal of part 1 was to check how many trees were visible from the outside. A tree is visible if it can reach an edge without running into another tree that is the same height or taller than it.

```python
def testVisible(tree, trees):
    good = True
    for x in trees:
        if x >= tree:
            good = False
            break
    return good
visibleCount = 0
for y in range(len(map)):
    if y == 0 or y == len(map) - 1:
        visibleCount += len(map[0])
        continue
    for x in range(len(map[0])):
        if x == 0 or x == len(map[0]) - 1:
            visibleCount += 1
            continue
        tree = int(map[y][x])
        left = [int(x) for x in map[y][:x]]
        right = [int(x) for x in map[y][x+1:]]
        up = [int(tx[x]) for tx in map[:y]]
        down = [int(tx[x]) for tx in map[y+1:]]

        l = testVisible(tree, reversed(left))
        r = testVisible(tree, right)
        u = testVisible(tree, reversed(up))
        d = testVisible(tree, down)

        if l or r or u or d:
            visibleCount += 1

print(visibleCount)
```

Part 2 was similar, but instead we had to find which tree had the highest "scenic score" which is just how far it can see in each cardinal direction multiplied by each other.
```python
def getViewDistance(tree, trees):
    distance = 0
    for x in trees:
        distance += 1
        if x >= tree:
            break
    return distance
maxScenicScore = float('-inf')
for y in range(len(map)):
    if y == 0 or y == len(map) - 1:
        continue
    for x in range(len(map[0])):
        if x == 0 or x == len(map[0]) - 1:
            continue
        tree = int(map[y][x])
        left = [int(x) for x in map[y][:x]]
        right = [int(x) for x in map[y][x+1:]]
        up = [int(tx[x]) for tx in map[:y]]
        down = [int(tx[x]) for tx in map[y+1:]]

        l = getViewDistance(tree, reversed(left))
        r = getViewDistance(tree, right)
        u = getViewDistance(tree, reversed(up))
        d = getViewDistance(tree, down)

        scenicScore = l * r * u * d
        if scenicScore > maxScenicScore:
            maxScenicScore = scenicScore

print(maxScenicScore)
```

