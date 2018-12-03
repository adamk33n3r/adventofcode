import re

def main():
    claims = {}
    with open('input.txt', 'r') as f:
        for line in f:
            boxId = line.rstrip('\n')
            matches = re.match(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', boxId)
            id, x, y, w, h = matches.groups()

            for x1 in range(int(x), int(x) + int(w)):
                for y1 in range(int(y), int(y) + int(h)):
                    if (x1, y1) not in claims:
                        claims[(x1, y1)] = 0
                    claims[(x1, y1)] += 1
        
        sqInches = 0
        for _, count in claims.items():
            if count >= 2:
                sqInches += 1
        print('The answer is', sqInches, 'in sq')

main()
