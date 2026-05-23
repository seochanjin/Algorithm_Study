import sys

input = sys.stdin.readline

n = int(input())
listA = list(map(int, input().split()))
m = int(input())
listB = list(map(int, input().split()))

listA.sort()
check = [0] * m

def solve(start, end, i):
    if start > end:
        return
    mid = (start + end)//2
    if listA[mid] == listB[i]:
        check[i]=1

    elif listA[mid] > listB[i]:
        solve(start, mid-1, i)

    else:
        solve(mid + 1, end, i)

for i in range(m):
    solve(0, n-1, i)
    print(check[i])