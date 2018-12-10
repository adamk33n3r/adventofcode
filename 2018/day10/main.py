import re

USE_EXAMPLE = False

with open('example.txt' if USE_EXAMPLE else 'input.txt', 'r') as f:

    points = []

    for line in f:
        matches = re.match(r'position=<(.+),(.+)> velocity=<(.+), (.+)>', line)
        px, py, vx, vy = map(int, matches.groups())

        points.append([px, py, vx, vy])

    s = 0
    lastDX = 1e10
    lastDY = 1e10
    while True:
        minX = min(points, key=lambda p: p[0])[0]
        minY = min(points, key=lambda p: p[1])[1]
        maxX = max(points, key=lambda p: p[0])[0]
        maxY = max(points, key=lambda p: p[1])[1]
        dx = maxX - minX
        dy = maxY - minY
        if lastDX < dx:
            # Go back one second
            s -= 1
            for point in points:
                point[0] -= point[2]
                point[1] -= point[3]
            minX = min(points, key=lambda p: p[0])[0]
            minY = min(points, key=lambda p: p[1])[1]
            maxX = max(points, key=lambda p: p[0])[0]
            maxY = max(points, key=lambda p: p[1])[1]
            for y in range(minY, maxY + 1):
                for x in range(minX, maxX + 1):
                    print('#' if (x, y) in [(p[0], p[1]) for p in points] else '.', end='')
                print()

            print(s)
            break

        s += 1
        lastDX = dx
        lastDY = dy

        for point in points:
            point[0] += point[2]
            point[1] += point[3]
