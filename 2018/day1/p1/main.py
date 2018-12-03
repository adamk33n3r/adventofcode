def main():
    acc = 0
    with open('input.txt', 'r') as f:
        for line in f:
            line = line.rstrip('\n')
            num = int(line)
            acc += num
            print(num, acc)
    print('Answer is', acc)

main()
