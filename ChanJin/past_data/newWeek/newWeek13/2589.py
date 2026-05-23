import sys
input = sys.stdin.readline
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]

def bfs(sx, sy):
    visited = [[-1] * m for _ in range(n)]
    q = deque([(sx, sy)])
    visited[sx][sy] = 0
    max_dist = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0<= ny < m:
                if graph[nx][ny] == 'L' and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    max_dist = max(max_dist, visited[nx][ny])
                    q.append((nx,ny))
    
    return max_dist

result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            result = max(result, bfs(i,j))

print(result)