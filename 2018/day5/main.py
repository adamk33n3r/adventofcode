def main():
    with open('input.txt', 'r') as f:
        polymer = f.readline().strip()

        stack = []
        for unit in polymer:
            if stack and stack[-1] != unit and stack[-1].upper() == unit.upper():
                stack.pop()
            else:
                stack.append(unit)
        print('P1:', len(stack))

        p2ans = len(stack)
        for letterToRemove in 'abcdefghijklmnopqrstuvqxyz':
            polymer2 = [c for c in polymer if c != letterToRemove.lower() and c != letterToRemove.upper()]
            stack = []
            for unit in polymer2:
                if stack and stack[-1] != unit and stack[-1].upper() == unit.upper():
                    stack.pop()
                else:
                    stack.append(unit)
            p2ans = min(p2ans, len(stack))

        print('P2:', p2ans)

main()
