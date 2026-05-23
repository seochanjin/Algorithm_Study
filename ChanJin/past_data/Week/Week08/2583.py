import sys
from collections import deque

input = sys.stdin.readline

m, n, k = map(int, input().split())
field = [[0]*n for _ in range(m)]


for i in range(k):
    a, b, c, d = map(int, input().split())
    for y in range(b, d):   
        for x in range(a, c):   
            field[y][x] = 1

visited = [[False]*n for _ in range(m)]
wtf = []

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def solve(x,y):
    deque_bfs = deque([(x, y)])
    visited[y][x] = True
    count = 0
    while(deque_bfs):
        x, y = deque_bfs.popleft()
        count += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if field[ny][nx] == 0 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    deque_bfs.append((nx, ny))
    return count

cnt = 0
for i in range(m):
    for j in range(n):
        if field[i][j] == 0 and not visited[i][j]:
            cnt+=1
            wtf.append(solve(j,i))

wtf.sort()
print(cnt)
for i in range(len(wtf)):
    print(wtf[i], end=' ')