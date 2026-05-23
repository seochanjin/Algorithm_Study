import sys, heapq

input = sys.stdin.readline

n, k = map(int, input().split())
jewel = [list(map(int, input().split())) for _ in range(n)]
bag = [int(input()) for _ in range(k)]

jewel.sort()
bag.sort()

result = 0
tmp_jewels = []
j_idx = 0

for bag_cap in bag:
    while j_idx < n and jewel[j_idx][0] <= bag_cap:
        heapq.heappush(tmp_jewels, -jewel[j_idx][1])
        j_idx += 1
    
    if tmp_jewels:
        result -= heapq.heappop(tmp_jewels)

print(result)