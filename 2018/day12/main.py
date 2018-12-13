import re

USE_EXAMPLE = False
exampleRes = [
    '...#..#.#..##......###...###...........',
    '...#...#....#.....#..#..#..#...........',
    '...##..##...##....#..#..#..##..........',
    '..#.#...#..#.#....#..#..#...#..........',
    '...#.#..#...#.#...#..#..##..##.........',
    '....#...##...#.#..#..#...#...#.........',
    '....##.#.#....#...#..##..##..##........',
    '...#..###.#...##..#...#...#...#........',
    '...#....##.#.#.#..##..##..##..##.......',
    '...##..#..#####....#...#...#...#.......',
    '..#.#..#...#.##....##..##..##..##......',
    '...#...##...#.#...#.#...#...#...#......',
    '...##.#.#....#.#...#.#..##..##..##.....',
    '..#..###.#....#.#...#....#...#...#.....',
    '..#....##.#....#.#..##...##..##..##....',
    '..##..#..#.#....#....#..#.#...#...#....',
    '.#.#..#...#.#...##...#...#.#..##..##...',
    '..#...##...#.#.#.#...##...#....#...#...',
    '..##.#.#....#####.#.#.#...##...##..##..',
    '.#..###.#..#.#.#######.#.#.#..#.#...#..',
    '.#....##....#####...#######....#.#..##.'
]

with open('example.txt' if USE_EXAMPLE else 'input.txt', 'r') as f:
    initialState = f.readline().rstrip()[15:]

    offset = 4
    pots = ['.'] * offset

    for state in initialState:
        pots.append(state)

    pots.append('.')
    pots.append('.')

    f.readline()
    patterns = {}
    for line in f:
        matches = re.match('([.#]{5}) => ([.#])', line)
        pattern, result = matches.groups()
        patterns[pattern] = result

    def main(generations):
        global pots, offset
        s = 0
        prevSum = 0
        prevDiff = 0
        stableCount = 0
        for gen in range(1, generations + 1):
            while ''.join(pots[:4]) != '....':
                pots.insert(0, '.')
                offset += 1
            while ''.join(pots[-4:]) != '....':
                pots.append('.')

            nextGenPots = pots.copy()

            for idx in range(2, len(pots)):
                pattern = ''.join(pots[idx-2:idx+3])
                while len(pattern) < 5:
                    # print('ASDF', pattern)
                    pattern += '.'
                res = patterns.get(pattern)
                pot = pots[idx] if idx < len(pots) else '.'
                if res:
                    # print(idx, pattern, pot, res)
                    nextGenPots[idx] = res
                else:
                    nextGenPots[idx] = '.'

            pots = nextGenPots.copy()
            # print(str(gen)+':', ''.join(pots))

            s = 0
            for idx, pot in enumerate(pots):
                idx -= offset
                if pot == '#':
                    s += idx
            if prevDiff == s - prevSum:
                # Found stable value candidate
                stableCount += 1
            if stableCount > 10:
                # Probably stable enough
                return s + (50000000000 - gen) * prevDiff

            prevDiff = s - prevSum
            prevSum = s

        return s

    print('P1:', main(20))
    print('P2:', main(50000000000))
