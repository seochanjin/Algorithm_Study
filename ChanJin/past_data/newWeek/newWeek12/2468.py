import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

max_h = max(map(max, graph))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y, h, visited):
    queue = deque([(x, y)])
    visited[x][y] = True

    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] > h and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

max_safe_area = 0

for h in range(max_h+1):
    visited = [[False]*n for _ in range(n)]
    cur_safe_area = 0

    for i in range(n):
        for j in range(n):
            if graph[i][j] > h and not visited[i][j]:
                bfs(i,j,h,visited)
                cur_safe_area += 1

    max_safe_area = max(max_safe_area, cur_safe_area)

print(max_safe_area)
