def main():
    acc = 0
    dic = {}
    with open('input.txt', 'r') as f:
        while acc not in dic or dic[acc] < 2:
            for line in f:
                line = line.rstrip('\n')
                num = int(line)
                acc += num
                print(num, acc)
                if acc not in dic:
                    dic[acc] = 0
                dic[acc] += 1

                if dic[acc] >= 2:
                    print('First reaches', acc, 'twice!')
                    break
            f.seek(0, 0)
        

main()
