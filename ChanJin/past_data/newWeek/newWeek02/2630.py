import sys

input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
count = [0, 0]


def solve(x, y, size):
    checkColor = paper[x][y]

    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != checkColor:
                half = size // 2
                solve(x, y, half)
                solve(x, y + half, half)
                solve(x + half, y, half)
                solve(x + half, y + half, half)
                return

    if checkColor == 0:
        count[0] += 1
    else:
        count[1] += 1


solve(0, 0, n)
print(count[0])
print(count[1])
