from collections import defaultdict, deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(m)]

adj = defaultdict(list)

for b, c in a:
    adj[b].append(c)
    adj[c].append(b)

bfs_visited = set()

def solve(start):
    bfs_deque = deque([start])
    bfs_visited.add(start)

    while(bfs_deque):
        top = bfs_deque.popleft()
        for b in adj[top]:
            if not b in bfs_visited:
                bfs_deque.append(b)
                bfs_visited.add(b)


cnt = 0
for i in range(1, n+1):
    if not i in bfs_visited:
        solve(i)
        cnt+=1

print(cnt)

