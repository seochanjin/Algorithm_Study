import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

empty = []
virus = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            empty.append((i, j))
        elif graph[i][j] == 2:
            virus.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
max_safe = 0

def get_safe_area(temp_graph):
    q = deque(virus)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if temp_graph[nx][ny] == 0:
                    temp_graph[nx][ny] = 2
                    q.append((nx, ny))
    
    count = 0
    for row in temp_graph:
        count += row.count(0)
    return count

def make_wall(count, start):
    global max_safe

    if count == 3:
        temp_graph = [row[:] for row in graph]
        max_safe = max(max_safe, get_safe_area(temp_graph))
        return
    
    for i in range(start, len(empty)):
        r, c = empty[i]
        graph[r][c] = 1
        make_wall(count + 1, i + 1)
        graph[r][c] = 0

make_wall(0, 0)
print(max_safe)