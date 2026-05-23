import sys, heapq
from collections import deque, defaultdict
input = sys.stdin.readline
adj = defaultdict(list)

n = int(input())
m = int(input())
line = [list(map(int, input().split())) for _ in range(m)]
start, end = map(int, input().split())

for a, b, c in line:
    adj[a].append((b,c))

result = 0
INF = int(1e9)
cnt = [INF] * (n+1)
cnt[start] = 0
heap = [(0, start)]

while heap:
    cost, node = heapq.heappop(heap)

    if cnt[node] < cost:
        continue
    for a, b in adj[node]:
        if cnt[a] > cost + b:
            cnt[a] = cost + b
            heapq.heappush(heap, (cnt[a], a))

print(cnt[end])