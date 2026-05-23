import sys

input = sys.stdin.readline

n, m = map(int, input().split())
tree = list(map(int, input().split()))
maxHigh = 0

def cutCheck(target):
    sumTree = 0
    for t in tree:
        if target < t:
            sumTree += t-target
    return sumTree


def solve(start, end):
    global maxHigh

    if start > end:
        return

    mid = (start + end)//2
    cutTree = cutCheck(mid)

    if cutTree >= m:
        maxHigh = mid
        solve(mid+1, end)
    else:
        solve(start, mid-1)


solve(0, max(tree))
print(maxHigh)