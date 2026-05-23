import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]

visited = [[[0]*2 for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque([(0, 0, 0)])
    visited[0][0][0] = 1

    while queue:
        x, y, wall_broken = queue.popleft()

        if x == n - 1 and y == m - 1:
            return visited[x][y][wall_broken]
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 0 and visited[nx][ny][wall_broken] == 0:
                    visited[nx][ny][wall_broken] = visited[x][y][wall_broken] + 1
                    queue.append((nx,ny,wall_broken))
                elif graph[nx][ny] == 1 and wall_broken == 0:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    queue.append((nx, ny, 1))

    return -1

print(bfs())