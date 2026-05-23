import sys
from collections import defaultdict, deque

input = sys.stdin.readline
adj = defaultdict(list)

comNum = int(input())
conNum = int(input())
edge = list(map(int, input().split()) for _ in range(conNum))

for a, b in edge:
    adj[a].append(b)
    adj[b].append(a)

for key in adj:
    adj[key].sort

visited = set()

def bfs(start):
    bfsDeque = deque([start])
    visited.add(start)

    while bfsDeque:
        top = bfsDeque.popleft()
        for b in adj[top]:
            if not b in visited:
                visited.add(b)
                bfsDeque.append(b)

bfs(1)
print(len(visited) - 1)