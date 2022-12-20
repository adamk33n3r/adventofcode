# Day 17

It's tetris! Part 1 had us drop 2022 blocks and find out what the highest point is.
```python
highestRock = 1

fallingRock = None
for _ in range(2023):
    if fallingRock:
        highestRock = min(highestRock, fallingRock.node.y - fallingRock.height + 1)
        fallingRock.destroy()
    spawnNode = m[2, highestRock - 4]
    fallingRock = Rock(nextRock(), spawnNode)
    while not fallingRock.atRest:
        # First, do wind
        inst = nextInstruction()
        if inst == '>':
            fallingRock.moveRight()
            pass
        elif inst == '<':
            fallingRock.moveLeft()
        # Then, fall
        fallingRock.moveDown()
print(-highestRock+1)
```
Part 2 wanted us to drop 10 trillion blocks. So in order to be able to do that, we had to find a way to skip ahead. We looked for patterns in the top so many blocks with the same instruction/block index and then we were able to calculate how far that would look like trillions into the future, and then run the last few blocks.

```python
fallingRock = None
rocksFallen = 0
TOTAL = 1000000000000
skippedHeight = 0
while rocksFallen < TOTAL:
    spawnNode = m[2, highestRock - 4]
    fallingRock = Rock(nextRock(rocksFallen), spawnNode)
    while not fallingRock.atRest:
        # First, do wind
        inst = nextInstruction()
        if inst == '>':
            fallingRock.moveRight()
            pass
        elif inst == '<':
            fallingRock.moveLeft()
        # Then, fall
        fallingRock.moveDown()
    ROCKS |= set([(u.node.x, u.node.y) for u in fallingRock.units])
    topRockFormation = frozenset([(x, -highestRock - -y) for x, y in ROCKS if -highestRock - -y <= 30])
    key = (instIdx, rocksFallen % 5, topRockFormation)
    miny = min([n.y for n in m.values() if n.type == '#'])
    if key in REPEAT:
        oldRocksFallen, oldHighestRock = REPEAT[key]
        cycleHeight = -miny - oldHighestRock
        cycleRockCount = rocksFallen - oldRocksFallen
        cyclesToSkip = (TOTAL - rocksFallen) // cycleRockCount
        skippedHeight += cyclesToSkip * cycleHeight
        rocksFallen += cyclesToSkip * cycleRockCount
    REPEAT[key] = (rocksFallen, -miny)
    rocksFallen += 1
    highestRock = min(highestRock, fallingRock.node.y - fallingRock.height + 1)
    fallingRock.destroy()

print(-highestRock+1 + skippedHeight)
```
