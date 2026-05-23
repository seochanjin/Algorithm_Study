import sys

input = sys.stdin.readline
result = 0

n, r, c = map(int, input().split())


def zLine(n, r, c):
    global result
    if n == 0:
        return

    halfLine = (2 ** n) // 2
    blockSize = halfLine ** 2

    if r < halfLine and c < halfLine:
        zLine(n - 1, r, c)
    elif r < halfLine and c >= halfLine:
        zLine(n - 1, r, c - halfLine)
        result += blockSize
    elif r >= halfLine and c < halfLine:
        zLine(n - 1, r - halfLine, c)
        result += 2 * blockSize
    else:
        zLine(n - 1, r - halfLine, c - halfLine)
        result += 3 * blockSize


zLine(n, r, c)
print(result)
