import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

visited = [[False]*m for _ in range(n)]


def solve(x,y):

    cnt = 1
    deque_bfs = deque([(x,y)])
    visited[x][y] = True

    while deque_bfs:
        x, y = deque_bfs.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if a[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    deque_bfs.append((nx, ny))
                    cnt+=1
    return cnt

count = 0
max_count = 0

for i in range(n):
    for j in range(m):
        if a[i][j] == 1 and not visited[i][j]:
            count += 1
            max_count = max(max_count,solve(i,j))

print(count)
print(max_count)

