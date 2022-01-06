class Vars:
    w,x,y,z = 0,0,0,0
def start():
    val = '9999999999'
    v = Vars()
    v.w = int(val[0])
    logic(v)

def logic(v: Vars):
    #x = 0
    v.x = v.z
    v.x %= 26
    v.z //= 1 # does 26 on 4,7,10,11,12,13,14
    v.x += 12 # variable
    v.x = 1 if v.x == v.w else 0
    v.x = 0 if v.x else 1
    v.y = 25
    v.y *= v.x
    v.y += 1
    v.z *= v.y

    v.y = v.w
    v.y += 4 # variable
    v.y *= v.x
    v.z += v.y

def startCode(val):
        # print(ret)
    # print('final:', ret)
    return ret

def logicCode(val, prev, idx):
    ret = prev
    tmp = prev
    tmp %= 26
    #ret //= 1 # does 26 on 4,7,10,11,12,13,14
    ret //= divs[idx]
    #tmp += 12 # variable number
    tmp += adds[idx]
    if 1<=tmp<=9:
        val = tmp
    elif divs[idx] == 26:
        print('get this above 0 and below 10:', tmp)

    matchesInput = tmp == val

    if not matchesInput:
        ret *= 26
        #ret += val + 4 # variable number
        ret += val + retadds[idx] # variable number
    if tmp <= 9 and tmp >= 1:
        # print('found', tmp, val, ret)
        return ret, tmp, True
    return ret, tmp, False



divs =    [ 1, 1, 1,26, 1, 1,26, 1, 1,26,26,26,26,26]
adds =    [12,11,14,-6,15,12,-9,14,14,-5,-9,-5,-2,-7]
retadds = [ 4,10,12,14, 6,16, 1, 7, 8,11, 8, 3, 1, 8]
n = 99999999999999
n = 99999299587349
n = [5,  1,  1,  1,  1,  6,  1,  1,  1,  1, 1,  1,  1,  1]
n = [9]*14
    #      $     $     $ $ $ $ $
    #1 2 3 4 5 6 7 8 9 1 1 1 1 1
                      #0 1 2 3 4
n = [1,9,1,7,8,3,9,9,6,9,7,3,9,9]
#greatest
n =    [ 9, 1, 3, 1, 8, 2, 1, 9, 6, 1, 1, 1, 1, 1]
#leastest
n =    [ 4, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1]

ret = 0
for idx in range(14):
    # vals = []
    # for i in range(1,10):
    #     vals.append(logicCode(i, ret, idx))
    # print(idx+1, vals, d)
    ret, goal, found = logicCode(n[idx], ret, idx)
    print(idx+1, idx in [3,6,9,10,11,12,13], [(ret//26**i)%26 for i in range(14)])
    if found:
        n[idx] = goal
    if idx == 12:
        print(n[idx])
    if adds[idx] < 10 and n[idx] != goal:
        print('breaking', adds[idx], n[idx], goal)
        break
if ret == 0:
    print('answer:', n, ret, ''.join(map(str, n)))
