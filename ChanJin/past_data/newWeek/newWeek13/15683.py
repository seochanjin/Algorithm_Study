import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

cctv_list = []
for i in range(n):
    for j in range(m):
        if 1 <= graph[i][j] <= 5:
            cctv_list.append((i, j, graph[i][j]))

mode = [
    [], 
    [[0], [1], [2], [3]],                
    [[0, 1], [2, 3]],                    
    [[0, 3], [0, 2], [1, 2], [1, 3]],    
    [[0, 1, 3], [0, 1, 2], [0, 2, 3], [1, 2, 3]], 
    [[0, 1, 2, 3]]                      
]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def watch(y, x, direction, temp_graph):
    for d in direction:
        ny, nx = y, x
        while True:
            ny+=dy[d]
            nx+=dx[d]
            if not (0<=ny<n and 0<=nx<m) or temp_graph[ny][nx] == 6:
                break
            if temp_graph[ny][nx] == 0:
                temp_graph[ny][nx] = '#'

min_value = float('inf')

def dfs(depth, current_graph):
    global min_value

    if depth == len(cctv_list):
        count = 0
        for row in current_graph:
            count += row.count(0)
        min_value = min(min_value, count)
        return
    
    y, x, cctv_type = cctv_list[depth]

    for direction in mode[cctv_type]:
        temp = [row[:] for row in current_graph]
        watch(y,x,direction, temp)
        dfs(depth + 1, temp)

dfs(0, graph)
print(min_value)
