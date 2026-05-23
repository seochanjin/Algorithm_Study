import sys
input = sys.stdin.readline

import heapq
from collections import defaultdict

INF = int(1e9)

v, e = map(int, input().split())
k = int(input())

adj = defaultdict(list)
for _ in range(e):
    u, v_dest, w = map(int, input().split())
    adj[u].append((v_dest, w))

distance = [INF] * (v+1)

def dij(start):
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for next_node, weight in adj[now]:
            cost = dist + weight

            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))

dij(k)

for i in range(1, v + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])