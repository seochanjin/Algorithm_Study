from collections import deque
import sys
input = sys.stdin.readline

m, n, h = map(int, input().split())
tomato = []
for i in range(h):
    c = []
    for j in range(n):
        b = list(map(int, input().split()))
        c.append(b)
    tomato.append(c)

dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

start=[]

def startCheck():
    for z in range(h):
        for y in range(n):
            for x in range(m):
                if tomato[z][y][x] == 1:
                    start.append((x,y,z))

maxCnt = 0

def bfs():
    bfsDeque = deque(start)
    
    while bfsDeque:
        x, y, z = bfsDeque.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0<=nx<m and 0<=ny<n and 0<=nz<h:
                if tomato[nz][ny][nx] == 0:
                    tomato[nz][ny][nx] = tomato[z][y][x] + 1
                    bfsDeque.append((nx, ny, nz))

def finalCheck():
    maxDay = 0
    for z in range(h):
        for y in range(n):
            for x in range(m):
                if tomato[z][y][x] == 0:
                    print(-1)
                    return
                maxDay = max(maxDay, tomato[z][y][x]-1)
    print(maxDay)

startCheck()
bfs()
finalCheck()