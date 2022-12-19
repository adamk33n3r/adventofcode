# Day 15

I honestly hated this one. The initial problem was cool, but the "puzzle" wasn't really what it seemed. The real puzzle was "how do you do this before the heat death of the universe" which I always hate. That's not a fun problem to solve for me. It took me 2 hours to get part 1 because the way I initially solved it was too slow for real input, even though it was immediate for the example. I was simulating each sensor, stepping through, and marking the spots that it hit. I had to rewrite the whole thing to just calculate the row we were looking for. And even then, it takes 3 minutes to run.

```python
y = 10 if USE_EXAMPLE else 2000000
count = 0
s = set()
r = 1000 if USE_EXAMPLE else 10000000 
for x in range(-r, r):
    n = m.get((x, y, 0))
    if n is not None and (n.type == 'B' or n.type == 'S'):
        continue
    good = True
    for sensor in sensors:
        d = distance((x, y), sensor.node.pos)
        if d <= sensor.distance:
            good = False
            break
    if not good:
        count += 1
```

At that point I gave up on part 2, it was late, and I honestly had no idea. Later that day, I was talking to a friend about it and discovered that there has to only be a single node within the range that isn't hit by any sensors. Because otherwise, it would be impossible to actually solve the problem. So knowing that, I just looped through each sensor and checked the nodes at distance + 1 to see if they are within range of any of the other sensors. If it isn't, then we've found our "hole". This ran way faster than part 1 coming in at 30 seconds lol.

```python
def findDistress():
    for sensor in sensors:
        # look on the edge of each sensors range
        # there has to only be one "hole", otherwise the problem would be impossible
        for sx, sy in [(1, 1), (-1, 1), (1, -1), (-1, -1)]:
            for x in range(sensor.distance + 1 + 1):
                y = sensor.distance + 1 - x

                # calculate position to check
                x2 = sensor.node.x + x * sx
                y2 = sensor.node.y + y * sy
                # skip if out of the range
                if x2 < 0 or x2 > 4000000 or y2 < 0 or y2 > 4000000:
                    continue

                good = True
                # Check if this point is within range of any other sensor
                # If it's not, then we've found it
                for sensor2 in sensors:
                    if sensor2 is sensor:
                        continue
                    d = distance((x2, y2), sensor2.node.pos)
                    if d <= sensor2.distance:
                        good = False
                        break
                if good:
                    return x2, y2
x, y = findDistress()
print(x * 4000000 + y)
```
