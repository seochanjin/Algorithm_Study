import sys
input = sys.stdin.readline
from collections import defaultdict,deque

r, c = map(int, input().split())
a = [list(map(str, input().strip())) for _ in range(r)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

d=[]
s=[]
w=[]
def serchStart():
    for i in range(r):
        for j in range(c):
            if a[i][j] == "D":
                d.append([i, j])
            if a[i][j] == "S":
                s.append([i, j])
            if a[i][j] == "*":
                w.append([i,j])

serchStart()

cnt = [[0]*c for _ in range(r)]

visited_s = [[False] * c for _ in range(r)]
visited_w = [[False] * c for _ in range(r)]

def bfs():
    dequeBfs = deque(s)
    dequeWater = deque(w)
    while dequeBfs:
        for _ in range(len(dequeWater)):
            e, t = dequeWater.popleft()
            for i in range(4):
                ne = e+dx[i]
                nt = t+dy[i]
                if 0<=ne<r and 0<=nt<c:
                    if a[ne][nt] == '.' and not visited_w[ne][nt]:
                        visited_w[ne][nt] = True
                        a[ne][nt] = '*'
                        dequeWater.append((ne, nt))

        for _ in range(len(dequeBfs)):
            x, y = dequeBfs.popleft()
            for j in range(4):
                nx = x + dx[j]
                ny = y + dy[j]
                if 0<=nx<r and 0<=ny<c:
                    if a[nx][ny] == 'D':
                        print(cnt[x][y] + 1)
                        return

                    if a[nx][ny] == '.' and not visited_s[nx][ny]:
                        visited_s[nx][ny] = True
                        dequeBfs.append((nx, ny))
                        cnt[nx][ny] = cnt[x][y] + 1
    print('KAKTUS')

bfs()
