import sys

input = sys.stdin.readline

aCount, bCount = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

totalCount = 0

for i in a:
    if i not in b:
        totalCount += 1

for i in b:
    if i not in a:
        totalCount += 1

print(totalCount)
