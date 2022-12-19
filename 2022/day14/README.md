# Day 14

Sand is falling into a cave and we want to simulate it! This one was pretty fun to watch run. The puzzle input is the layout of the rocks of the cave the sand will fall through. But not how it usually does it by having it written out in text. It's written out in a list of line instructions. Like `476,60 -> 476,61 -> 489,61`.

Part one wants us to report how many units of sand come to rest before the sand starts falling into the void.

Part two places a floor plane below the map and asks us how many units of sand come to rest before the source of the sand at the top gets blocked by sand building up.

In both parts, I used my `Map` library to simulate the sand. Every time I've used `Map` this year, I've used the `Default` variants of the adjacent node properties. I wonder if that should just be the behavior. Do I need to "get" the left node if its null? I could just check if the left node's type is default. Could be a nice upgrade so that there arent soooo many properties.

```python
SAND = Node(m, (500, 0), '+')
AIR = '.'
restCount = 0
FLOOR = 2 + m.maxY
while True:
    newSand = Unit('o', SAND)
    void = False
    while True:
        if newSand.node.pos[1] == FLOOR - 1:
            restCount += 1
            newSand.node.type = 'S'
            break
        if newSand.node.downDefault.type == AIR:
            newSand.node = newSand.node.downDefault
        elif newSand.node.leftDownDefault.type == AIR:
            newSand.node = newSand.node.leftDownDefault
        elif newSand.node.rightDownDefault.type == AIR:
            newSand.node = newSand.node.rightDownDefault
        else:
            restCount += 1
            newSand.node.type = 'S'
            break
    if SAND.type == 'S':
        break
print(restCount)
```
