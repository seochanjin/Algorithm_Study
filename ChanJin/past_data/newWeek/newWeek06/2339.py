import sys

input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]


def solve(x1, y1, x2, y2, direction):
    jewels = []
    impurities = []

    for i in range(x1, x2):
        for j in range(y1, y2):
            if board[i][j] == 2:
                jewels.append((i, j))
            elif board[i][j] == 1:
                impurities.append((i, j))

    jewelsCount = len(jewels)
    if jewelsCount == 0: return 0
    if jewelsCount == 1:
        if len(impurities) == 0:
            return 1
        else:
            return 0
    if len(impurities) == 0: return 0

    res = 0

    for r, c in impurities:
        if direction != 1:
            canCut = True
            for j in range(y1, y2):
                if board[r][j] == 2:
                    canCut = False
                    break
            if canCut:
                res += solve(x1, y1, r, y2, 1) * solve(r + 1, y1, x2, y2, 1)

        if direction != 0:
            canCut = True
            for i in range(x1, x2):
                if board[i][c] == 2:
                    canCut = False
                    break
            if canCut:
                res += solve(x1, y1, x2, c, 0) * solve(x1, c + 1, x2, y2, 0)

    return res


answer = solve(0, 0, n, n, 2)
if answer > 0:
    print(answer)
else:
    print(-1)