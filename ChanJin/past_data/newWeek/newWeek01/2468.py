import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x,y,h):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n:
            if not visited[nx][ny] and array[nx][ny] > h:
                dfs(nx, ny, h)


maxSafe = 0
for h in range(1, 101):
    visited = [[False] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and array[i][j] > h:
                dfs(i,j,h)
                count += 1
    maxSafe = max(maxSafe, count)

print(maxSafe)