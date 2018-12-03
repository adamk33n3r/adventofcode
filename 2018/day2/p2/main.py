def main():
    boxIds = []
    with open('input.txt', 'r') as f:

        result = ''

        for line in f:
            boxId = line.rstrip('\n')

            for compBoxId in boxIds:
                diffCount = 0
                for i in range(26):
                    if boxId[i] is not compBoxId[i]:
                        diffCount += 1
                    if diffCount > 1:
                        break
                if diffCount is 1:
                    print(boxId, compBoxId)
                    for i in range(26):
                        if boxId[i] is not compBoxId[i]:
                            continue
                        result += boxId[i]

            boxIds.append(boxId)

        print('The result is', result)

main()
