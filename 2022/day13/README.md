# Day 13

Day 13 was having us check if pairs of packets were in the correct order. The packets come as nested lists of numbers. The rules we got were a little confusing, and it took me a long time to figure out what was actually asked. Basically, we check numbers in the same nested level of lists from each packet of the pair. If they are the same, we continue to the next numbers. If the left number is more than the right, the packets are NOT in order. If the left is less than the right, then the packets ARE in order. The issue I was having was I was under the impression that we had to check if ALL of the numbers are in the right order i.e. every number in the left packet is less than its pair in the right packet. This turned out to be false, and as soon as you find a pair of numbers that aren't the same then you know if it's correct or not.

While it sounds simple enough, the nested lists made it a little complicated. Here is the compare function I wrote.
```python
def cmp(a, b):
    # print('left:', a, 'right:', b)
    la, lb = len(a), len(b)
    for i in range(min(la, lb)):
        a1, b1 = a[i], b[i]
        if type(a1) == int and type(b1) == int:
            if a1 > b1:
                return False
            elif a1 < b1:
                return True
        elif type(a1) == list and type(b1) == list:
            res = cmp(a1, b1)
            if res == False:
                return False
            elif res == True:
                return True
        else:
            if type(a1) == list:
                res = cmp(a1, [b1])
                if res == False:
                    return False
                elif res == True:
                    return True
            else:
                res = cmp([a1], b1)
                if res == False:
                    return False
                elif res == True:
                    return True
    if la < lb:
        return True
    elif lb < la:
        return False
    return None
```
Part one wanted us to sum the indicies of the packets that are already ordered correctly.

For part two, it wanted us to actually sort the packets, so I just passed it into `sorted()` as `key=` using `cmp_to_key()`
