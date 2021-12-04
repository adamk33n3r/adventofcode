USE_EXAMPLE = False
PRINT_DEBUG = False

with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    prev = None
    count = 0
    for line in file:
        line = int(line.strip())
        if prev is None:
            prev = line
            continue
        if line > prev:
            count = count + 1
        prev = line
    print(count)

with open('example.txt' if USE_EXAMPLE else 'input.txt') as file:
    slide = []
    curWindow = 0
    idx = 0
    depths = [int(line.strip()) for line in file]
    for idx in range(len(depths)):
        if len(slide) <= curWindow + 2:
            slide.append([])
            slide.append([])
            slide.append([])
        slide[curWindow].append(depths[idx])
        if idx > 0 and idx + 1 < len(depths):
            slide[curWindow+1].append(depths[idx])
        if idx > 1 and idx + 2 < len(depths):
            slide[curWindow+2].append(depths[idx])
        if len(slide[curWindow]) == 3:
            curWindow = curWindow + 1

        idx = idx + 1
    prev = None
    count = 0
    for window in slide:
        s = sum(window)
        if prev is None:
            prev = s
            continue
        if s > prev:
            count = count + 1
        prev = s
    print(count)
