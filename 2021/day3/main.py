USE_EXAMPLE = False
PRINT_DEBUG = False

gamma = ''
epsilon = ''
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    bits = [line.strip() for line in file]
    for idx in range(len(bits[0])):
        s = sum([int(bit[idx]) for bit in bits])
        gamma += '1' if s > len(bits) / 2 else '0'
        epsilon += '0' if s > len(bits) / 2 else '1'

    print(int(gamma, 2) * int(epsilon, 2))

ogr = 0
csr = 0
with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    bits = [line.strip() for line in file]

    # ogr
    idx = 0
    copy = bits[:]
    for idx in range(len(bits[0])):
        s = sum([int(bit[idx]) for bit in copy])
        common  = '1' if s >= len(copy) / 2 else '0'
        for bit in bits:
            if bit[idx] != common:
                if bit in copy:
                    copy.remove(bit)
        if len(copy) == 1:
            ogr = int(copy[0], 2)
            break

    # csr
    idx = 0
    copy = bits[:]
    for idx in range(len(bits[0])):
        s = sum([int(bit[idx]) for bit in copy])
        common  = '0' if s >= len(copy) / 2 else '1'
        for bit in bits:
            if bit[idx] != common:
                if bit in copy:
                    copy.remove(bit)
        if len(copy) == 1:
            csr = int(copy[0], 2)
            break
    print(ogr * csr)
