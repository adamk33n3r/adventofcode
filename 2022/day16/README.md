# Day 16

This problem was kinda fun, we had to figure out which path through a series of opening valves is the most optimal. My original solution was "try them all and pick the best one". There's "only" 15 valves that you need to try. What I didn't realize is that that means there are over 1 trillion different permutations to try. Ya, too slow.

So after looking at some of the results while running, I noticed that it seemed that the most valves you'd visit before time ran out was 7, so instead of 15C15 I did 15C7 which only resulted in like 30 million paths to explore!

I grabbed all of the valves that had a rate more than 0 and then called `permutations` with them asking for `7`. For each one, I calculated how many it could reach in that path, and then calculated the total flow that that path would get.

```python
memoized = {}
def getRates(start, path, minutes):
    if path in memoized:
        return memoized[path]
    totalTime = 0
    rates = []
    prev = start
    for v in path:
        costToValve = prev.costs[v]
        # Check if moving there and opening would take too long
        if totalTime + costToValve + 1 > minutes:
            continue
        # Cost to move there + open
        totalTime += costToValve + 1
        rates.append((v, costToValve + 1, v.rate))
        prev = v
    memoized[path] = tuple(rates)
    return tuple(rates)

def findMostPressure(valves, valve: Valve, minutes):
    def processRatePath(ratePath):
        if ratePath in memoized:
            return memoized[ratePath]
        t = minutes
        valveStates = {}
        def tick(timeToUse):
            for v in valveStates:
                vs = valveStates[v]
                valveStates[v] = (vs[0], vs[1]+vs[0]*timeToUse)

        for valve, timeToUse, rate in ratePath:
            t -= timeToUse
            tick(timeToUse)

            valveStates[valve] = (rate, 0)
        tick(t)
        res = sum([v[1] for v in valveStates.values()])
        memoized[ratePath] = res
        return res

    valvesWithRate: list[Valve] = list(filter(lambda v: v.rate > 0 and v.closed == True, valves.values()))
    perms = permutations(valvesWithRate, 7)
    maxFlow = float('-inf')
    for i, permutation in enumerate(perms):
        ratePath = getRates(valve, permutation, minutes)
        totalFlow = processRatePath(ratePath)
        if totalFlow > maxFlow:
            maxFlow = totalFlow
            print('new maxFlow1:', maxFlow)
        if i % 1000000 == 0:
            print(i)
    return maxFlow
```
It was still pretty slow, and for part 2 it was way too slow. So the next day, I rewrote it with recursion and it was so much simpler! :P
```python
memoized = {}
def findMostPressure(valves, valve: Valve, valveState, minutes, elephant):
    if minutes == 0:
        return 0 if not elephant else findMostPressure(valves, valves['AA'], valveState, 26, False)
    memkey = (valve, valveState, minutes, elephant)
    if memkey in memoized:
        return memoized[memkey]

    ans = 0
    # If true, try opening this valve
    if valveState[valve.idx] == False and valve.rate > 0:
        # Scores from the next minute on
        valveScore = (minutes - 1) * valve.rate
        ans = max(ans, valveScore + findMostPressure(valves, valve, tuple([(True if i == valve.idx else s) for i,s in enumerate(valveState)]), minutes-1, elephant))
    
    # Try moving to connected valves
    for adj in valve.tunnels:
        ans = max(ans, findMostPressure(valves, adj, valveState, minutes-1, elephant))

    memoized[memkey] = ans
    return ans
```
