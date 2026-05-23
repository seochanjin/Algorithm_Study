import sys
input = sys.stdin.readline

n = int(input())
solList = list(map(int, input().split()))
solList.sort()
bestList = [solList[0], solList[n-1]]

def solve(start, end):
    while start < end:
        mid = solList[start] + solList[end]

        if mid == 0:
            bestList[0] = solList[start]
            bestList[1] = solList[end]
            break

        elif mid > 0:
            if abs(mid) < abs(bestList[0]+bestList[1]):
                bestList[0] = solList[start]
                bestList[1] = solList[end]
            end -= 1

        else:
            if abs(mid) < abs(bestList[0] + bestList[1]):
                bestList[0] = solList[start]
                bestList[1] = solList[end]
            start += 1


solve(0, n-1)
print(bestList[0], bestList[1])