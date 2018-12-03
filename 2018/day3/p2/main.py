import re

def main():
    claims2 = {}
    with open('input.txt', 'r') as f:
        for line in f:
            boxId = line.rstrip('\n')
            matches = re.match(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', boxId)
            id, x, y, w, h = matches.groups()

            claims2[id] = { 'x': int(x), 'y': int(y), 'w': int(w), 'h': int(h) }
        
        claimsThatOverlap = []
        for id, claim in claims2.items():
            for id2, claim2 in claims2.items():
                if id is id2:
                    continue
                isOverlapping = claim['x'] < claim2['x'] + claim2['w'] and \
                claim['x'] + claim['w'] > claim2['x'] and \
                claim['y'] < claim2['y'] + claim2['h'] and \
                claim['y'] + claim['h'] > claim2['y']

                if isOverlapping:
                    claimsThatOverlap.append(int(id))
                    claimsThatOverlap.append(int(id2))

        # Assumes ids are sequential
        
        claimsThatOverlap = sorted(list(set(claimsThatOverlap)))

        for i in range(1, claimsThatOverlap[len(claimsThatOverlap) - 1]):
            if i not in claimsThatOverlap:
                print('No overlaps', i)
                break

main()
