import sys
from collections import deque
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
m = int(input())
a = [list(map(int, input().split())) for _ in range(m)]

adj = defaultdict(list)

for a, b in a:
    adj[a].append(b)
    adj[b].append(a)

bfs_visited = set()

def solve(start):

    bfs_visited.add(start)
    bfs_deque = deque([start])

    while(bfs_deque):
        top = bfs_deque.popleft()
        for b in adj[top]:
            if not b in bfs_visited:
                bfs_deque.append(b)
                bfs_visited.add(b)

solve(1)
print(len(bfs_visited) - 1)