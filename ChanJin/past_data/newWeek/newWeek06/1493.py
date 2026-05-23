import sys

input = sys.stdin.readline

l, w, h = map(int, input().split())
n = int(input())
boxList = [list(map(int, input().split())) for _ in range(n)]

boxList.sort(reverse=True)

totalCount = 0
filledVolume = 0

for i, count in boxList:
    side = 2 ** i

    maxCanFill = (l // side) * (w // side) * (h // side)
    newFillNeed = maxCanFill - (filledVolume * 8)

    actualFill = min(count, newFillNeed)

    totalCount += actualFill
    filledVolume = (filledVolume * 8) + actualFill

if filledVolume == l * w * h:
    print(totalCount)
else:
    print(-1)
