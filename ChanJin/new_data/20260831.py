from collections import deque

def solution(board):
    m = len(board)
    n = len(board[0])
    
    start = end = None
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'R':
                start = (i, j)
            elif board[i][j] == 'G':
                end = (i, j)
    
    def slide(x, y, dx, dy):
        while True:
            nx, ny = x + dx, y + dy
            if not (0<=nx<m and 0<=ny<n) or board[nx][ny] == 'D':
                break
            x, y = nx, ny
        return x, y
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    visited = [[False]*n for _ in range(m)]
    visited[start[0]][start[1]] = True
    queue = deque([(start[0], start[1], 0)])
    
    while queue:
        x, y, count = queue.popleft()
        
        if (x, y) == end:
            return count
        
        for i in range(4):
            nx, ny = slide(x, y, dx[i], dy[i])
            if not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, count + 1))

    return -1