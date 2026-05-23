import sys

input = sys.stdin.readline

cityCount = int(input())
costArray = [list(map(int, input().split())) for _ in range(cityCount)]

visitCity = [False] * cityCount
minCost = sys.maxsize


def costCount(now, cost, depth):
    global minCost

    if depth == 1:
        if costArray[now][0] != 0:
            minCost = min(costArray[now][0] + cost, minCost)
        return

    if cost > minCost:
        return

    for nextCity in range(cityCount):
        if costArray[now][nextCity] != 0 and not visitCity[nextCity]:
            visitCity[nextCity] = True
            costCount(nextCity, cost+costArray[now][nextCity], depth - 1)
            visitCity[nextCity] = False


visitCity[0] = True
costCount(0, 0, cityCount)
print(minCost)

## 연습 ##
# def dfs(now, cost, depth):
#     global minCost
#     if depth == 1:
#         if costArray[now][0] != 0:
#             minCost = min(costArray[now][0] + cost, minCost)
#             return
#
#     if cost > minCost:
#         return
#
#     for nextCity in range(cityCount):
#         if costArray[now][nextCity] != 0 and not visitCity[nextCity]:
#             visitCity[nextCity] = True
#             dfs(nextCity, cost+costArray[now][nextCity], depth - 1)
#             visitCity[nextCity] = False
