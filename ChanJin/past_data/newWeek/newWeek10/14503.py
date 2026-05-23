import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r,c,d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

count = 0

while True:
    if board[r][c] == 0:
        board[r][c] = 2
        count += 1

    has_empty = False
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < n and 0 <= nc < m:
            if board[nr][nc] == 0:
                has_empty = True
                break

    if has_empty:
        for _ in range(4):
            d = (d+3) % 4
            nr, nc = r + dr[d], c + dc[d]

            if 0 <= nr < n and 0 <= nc < m and board[nr][nc] == 0:
                r, c = nr, nc
                break

    else:
        br, bc = r - dr[d], c - dc[d]

        if 0 <= br < n and 0 <= bc < m and board[br][bc] != 1:
            r, c = br, bc
        else:
            break

print(count)