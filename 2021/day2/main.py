USE_EXAMPLE = False
PRINT_DEBUG = False

x = 0
y = 0
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    for line in file:
        dir, dist = line.split(' ')
        if dir == 'forward':
            x += int(dist)
        elif dir == 'up':
            y -= int(dist)
        elif dir == 'down':
            y += int(dist)
    print(x * y)

x = 0
y = 0
aim = 0
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    for line in file:
        dir, dist = line.split(' ')
        if dir == 'forward':
            x += int(dist)
            y += aim * int(dist)
        elif dir == 'up':
            aim -= int(dist)
        elif dir == 'down':
            aim += int(dist)
    print(x * y)
