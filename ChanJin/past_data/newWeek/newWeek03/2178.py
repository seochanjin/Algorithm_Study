from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

visited = [[False]*m for _ in range(n)]
count = [[0]*m for _ in range(n)]

def bfs(a, b):
    bfsDeque = deque([(a, b)])
    visited[a][b] = True
    count[a][b] += 1

    while bfsDeque:
        x, y = bfsDeque.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if not visited[nx][ny] and maze[nx][ny] == 1:
                    visited[nx][ny] = True
                    count[nx][ny] = count[x][y] + 1
                    bfsDeque.append((nx, ny))

bfs(0,0)
print(count[n-1][m-1])