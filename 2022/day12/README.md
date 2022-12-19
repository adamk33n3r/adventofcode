# Day 12

Day 12 was a simple dijkstra algorithm but my pea brain forgot that that was a thing, let alone one that I had implemented in my map libaray lol.

We had to find a path from `S` to `E` going through different nodes based on letters. We can go up one letter from where we are and "down" any amount of letters.

```python
def findPath(end, path: deque[Tuple[int, Node]]):
    visited = set()
    distance = 0
    while path:
        distance, node = path.popleft()
        if node in visited:
            continue
        visited.add(node)
        if node == end:
            return distance
        for adj in node.adj:
            if ord(adj.type) - ord(node.type) <= 1:
                path.append((distance + 1, adj))
    return -1
```

Part 2 wanted us to look at more starts, so including elevation `a`.
