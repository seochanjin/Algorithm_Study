import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

a = [list(map(str, input().strip())) for _ in range(n)]


visited = [[False] * m for _ in range(n)]


def solve(x, y):
    deque_bfs = deque([(x, y)])
    visited[x][y] = True
    while(deque_bfs):
        x, y = deque_bfs.popleft()

        if a[x][y] == '-':
            for dy in [-1, 1]:
                ny = y + dy
                if 0<=ny<m:
                    if a[x][ny] == '-' and not visited[x][ny]:
                        visited[x][ny] = True
                        deque_bfs.append((x, ny))
        elif a[x][y] == '|':
            for dx in [-1, 1]:
                nx = x + dx
                if 0<=nx<n:
                    if a[nx][y] == '|' and not visited[nx][y]:
                        visited[nx][y] = True
                        deque_bfs.append((nx, y))
        

count = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == False:
            solve(i, j)
            count += 1

print(count)
            
