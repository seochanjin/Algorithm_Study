import sys

input = sys.stdin.readline

n, c = map(int, input().split())
x = [int(input()) for _ in range(n)]
x.sort()


def solve(mid):
    cnt = 1
    last = x[0]

    for i in range(1, n):
        if x[i] - last >= mid:
            cnt += 1
            last = x[i]
    return cnt >= c


def serch(start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2

        if solve(mid):
            result = mid
            start = mid + 1

        else:
            end = mid - 1

    return result


print(serch(1, x[-1] - x[0]))