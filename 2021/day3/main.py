USE_EXAMPLE = False
PRINT_DEBUG = False

gamma = ''
epsilon = ''
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    report = [line.strip() for line in file]
    for idx in range(len(report[0])):
        s = sum([int(bits[idx]) for bits in report])
        gamma += '1' if s > len(report) / 2 else '0'
        epsilon += '0' if s > len(report) / 2 else '1'

    print(int(gamma, 2) * int(epsilon, 2))

ogr = 0
csr = 0
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    report = [line.strip() for line in file]

    # ogr
    idx = 0
    copy = report[:]
    for idx in range(len(report[0])):
        s = sum([int(bits[idx]) for bits in copy])
        common  = '1' if s >= len(copy) / 2 else '0'
        for bits in report:
            if bits[idx] != common:
                if bits in copy:
                    copy.remove(bits)
        if len(copy) == 1:
            ogr = int(copy[0], 2)
            break

    # csr
    idx = 0
    copy = report[:]
    for idx in range(len(report[0])):
        s = sum([int(bits[idx]) for bits in copy])
        common  = '0' if s >= len(copy) / 2 else '1'
        for bits in report:
            if bits[idx] != common:
                if bits in copy:
                    copy.remove(bits)
        if len(copy) == 1:
            csr = int(copy[0], 2)
            break
    print(ogr * csr)
