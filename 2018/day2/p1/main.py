def main():
    boxIds = { 2: [], 3: [] }
    with open('input.txt', 'r') as f:
        for line in f:
            boxId = line.rstrip('\n')

            letters = {}

            for letter in boxId:
                if letter not in letters:
                    letters[letter] = 0
                letters[letter] += 1

            countsAs2 = False
            countsAs3 = False
            for letter, count in letters.items():
                if count is 2:
                    countsAs2 = True
                elif count is 3:
                    countsAs3 = True

            if countsAs2:
                boxIds[2].append(boxId)
            if countsAs3:
                boxIds[3].append(boxId)

        print('The checksum is', len(boxIds[2]) * len(boxIds[3]))

main()
