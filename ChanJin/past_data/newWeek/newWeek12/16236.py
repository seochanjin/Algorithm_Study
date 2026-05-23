import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

cur_x, cur_y = 0, 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            cur_x, cur_y = i , j
            graph[i][j] = 0

shark_size = 2
eaten_count = 0
total_time = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def find_fish(sx, sy, size):
    distances = [[-1]* n for _ in range(n)]
    q = deque([(sx, sy)])
    distances[sx][sy] = 0
    readable_fishes = []

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and distances[nx][ny] == -1:
                if graph[nx][ny] <= size:
                    distances[nx][ny] = distances[x][y] + 1
                    q.append((nx, ny))
                    if 0 < graph[nx][ny] < size:
                        readable_fishes.append((distances[nx][ny], nx, ny))

    if not readable_fishes:
        return None
    readable_fishes.sort()
    return readable_fishes[0]

while True:
    result = find_fish(cur_x, cur_y, shark_size)

    if result is None:
        break

    dist,nx,ny = result
    total_time += dist
    cur_x, cur_y = nx, ny
    graph[nx][ny] = 0

    eaten_count += 1
    if eaten_count == shark_size:
        shark_size += 1
        eaten_count = 0

print(total_time)
