import sys
from collections import deque
input = sys.stdin.readline

def sol(x,y):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    deque_bfs = deque([(x,y)])
    visited[y][x] = True

    while(deque_bfs):
        px, py = deque_bfs.popleft()
        for i in range(4):
            nx = px + dx[i]
            ny = py + dy[i]
            if 0<=nx<m and 0<=ny<n:
                if graph[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    deque_bfs.append((nx, ny))

t = int(input())

for i in range(t):

    cnt = 0

    m, n, k = map(int, input().split())
    visited = [[False]*m for _ in range(n)]
    graph = [[0]*m for _ in range(n)]
    for i in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    for j in range(n):
        for i in range(m):
            if graph[j][i] == 1 and not visited[j][i]:
                cnt += 1
                sol(i, j)
    
    print(cnt)

