import sys
from collections import deque;

input = sys.stdin.readline

def solve(x, y):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]



    deque_bfs = deque([(x, y)])
    visited[y][x] = True

    while(deque_bfs):
        x, y = deque_bfs.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<m and 0<=ny<n:
                if field[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    deque_bfs.append((nx, ny))

t = int(input())

for i in range(t):
    cnt = 0
    
    m, n, k = map(int, input().split())
    field = [[0]*m for _ in range(n)]
    visited = [[False]*m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        field[y][x] = 1

    for j in range(n):
        for i in range(m):
            if field[j][i] == 1 and not visited[j][i]:
                cnt+=1
                solve(i,j)

    print(cnt)

