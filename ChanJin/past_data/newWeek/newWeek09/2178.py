import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
map_list = [list(map(int, input().strip())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]
count = [[0] * m for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def sol(a, b):
    bfs_queue = deque([(a,b)])
    visited[a][b] = True
    count[a][b] += 1

    while bfs_queue:
        x, y = bfs_queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0<= ny<m:
                if not visited[nx][ny] and map_list[nx][ny] == 1:
                    bfs_queue.append((nx, ny))
                    visited[nx][ny] = True
                    count[nx][ny] = count[x][y] + 1

sol(0,0)
print(count[n-1][m-1])
