from collections import deque

def bfs(start, maps, n, m):
    dist = [[-1] * m for _ in range(n)]
    dist[start[0]][start[1]] = 0
    queue = deque([start])
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] != 'X' and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))
        
    return dist

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    start = lever = exit_pos = None    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                start = (i, j)
            elif maps[i][j] == 'L':
                lever = (i, j)
            elif maps[i][j] == 'E':
                exit_pos = (i, j)
    
    dist_from_start = bfs(start, maps, n, m)
    dist_from_lever = bfs(lever, maps, n, m)
    
    d1 = dist_from_start[lever[0]][lever[1]]
    d2 = dist_from_lever[exit_pos[0]][exit_pos[1]]
    
    if d1 == -1 or d2 == -1:
        return -1
    
    
    return d1 + d2