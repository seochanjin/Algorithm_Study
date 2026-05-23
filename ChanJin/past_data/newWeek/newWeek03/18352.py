import sys
input = sys.stdin.readline
from collections import deque, defaultdict
adj = defaultdict(list)

n, m, k, x = map(int, input().split())
route = [list(map(int, input().split())) for _ in range(m)]

for a, b in route:
    adj[a].append(b)

cnt = [0]*(n+1)

def bfs(start):
    visited = set()
    bfsDeque = deque([start])
    visited.add(start)

    while bfsDeque:
        top = bfsDeque.popleft()

        for i in adj[top]:
            if not i in visited:
                cnt[i]+=cnt[top]+1
                visited.add(i)
                bfsDeque.append(i)

bfs(x)

for i in range(len(cnt)):
    if cnt[i] == k:
        print(i)

if not k in cnt:
    print(-1)