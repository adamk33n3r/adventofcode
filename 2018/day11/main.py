from collections import defaultdict
serial = 6392

grid = defaultdict(int)
for x in range(1, 301):
    for y in range(1, 301):
        rackID = x + 10
        power = rackID * y
        power += serial
        power *= rackID
        power //= 100
        power = int(str(power)[-1])
        power -= 5
        grid[(x, y)] = power

greatestPower = 0
coord = None
for x in range(1, 301 - 2):
    for y in range(1, 301 - 2):
        p = 0
        p += grid[(x, y)]
        p += grid[(x+1, y)]
        p += grid[(x+2, y)]

        p += grid[(x, y+1)]
        p += grid[(x+1, y+1)]
        p += grid[(x+2, y+1)]

        p += grid[(x, y+2)]
        p += grid[(x+1, y+2)]
        p += grid[(x+2, y+2)]

        if p > greatestPower:
            greatestPower = p
            coord = (x, y)

print('P1:', coord)

# Part 2

greatestPower = 0
s = 0
coord = None

for x in range(1, 301):
    for y in range(1, 301):
        prevSizePower = None
        for size in range(1, 301 - max(x, y)):
            p = 0

            if prevSizePower is not None:
                p += prevSizePower
                for dx in range(size):
                    p += grid[(x + dx, y + size - 1)]
                for dy in range(size):
                    p += grid[(x + size - 1, y + dy)]
            else:
                p += grid[(x, y)]
            
            prevSizePower = p

            if p > greatestPower:
                greatestPower = p
                coord = (x, y)
                s = size

print(greatestPower, s, coord)
