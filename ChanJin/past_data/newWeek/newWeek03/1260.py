import sys
from collections import defaultdict, deque

input = sys.stdin.readline
adj = defaultdict(list)
n, m, v = map(int, input().split())
edge = list(map(int, input().split()) for _ in range(m))

for a, b in edge:
    adj[a].append(b)
    adj[b].append(a)

for key in adj:
    adj[key].sort()

visited = set()

def dfs(start):
    visited.add(start)
    print(start, end = ' ')
    for b in adj[start]:
        if not b in visited:
            dfs(b)

def bfs(start):
    visitedBfs = set()
    bfsDeque = deque([start])
    visitedBfs.add(start)

    while bfsDeque:
        top = bfsDeque.popleft()
        print(top, end=' ')
        for b in adj[top]:
            if not b in visitedBfs:
                visitedBfs.add(b)
                bfsDeque.append(b)

dfs(v)
print()
bfs(v)
