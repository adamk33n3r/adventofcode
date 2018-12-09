from collections import defaultdict, deque
import re

USE_EXAMPLE = False
PRINT_DEBUG = False

def play(marbleCount):

    scores = defaultdict(int)

    marbleCircle = deque([0])
    for marbleNum in range(1, marbleCount + 1):
        if marbleNum % 23 == 0:
            marbleCircle.rotate(-7)
            removed = marbleCircle.popleft()
            scores[marbleNum % numPlayers] += marbleNum + removed
            marbleCircle.rotate(1)
        else:
            marbleCircle.rotate(1)
            marbleCircle.appendleft(marbleNum)

    print(max(scores.values(), key=lambda score: score))

with open('example.txt' if USE_EXAMPLE else 'input.txt', 'r') as f:
    line = f.readline()
    matches = re.match(r'(\d+) players; last marble is worth (\d+) points', line)

    numPlayers, marbleCount = map(int, matches.groups())

    print('P1: ', end='')
    play(marbleCount)
    print('P2: ', end='')
    play(marbleCount * 100)
