import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
houses = []
chickens = []

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 1:
            houses.append((i, j))
        elif row[j] == 2:
            chickens.append((i, j))

min_total_dist = float('inf')

for selected_chickens in combinations(chickens, m):
    total_dist = 0
    
    # 3. 각 집마다 가장 가까운 치킨집 찾기
    for hx, hy in houses:
        dist_to_nearest = float('inf')
        for cx, cy in selected_chickens:
            # 맨해튼 거리 공식: |x1-x2| + |y1-y2|
            dist = abs(hx - cx) + abs(hy - cy)
            dist_to_nearest = min(dist_to_nearest, dist)
        
        total_dist += dist_to_nearest
        
        # 중간에 이미 최솟값을 넘었다면 더 계산할 필요 없음 (가지치기)
        if total_dist >= min_total_dist:
            break
            
    min_total_dist = min(min_total_dist, total_dist)

print(min_total_dist)