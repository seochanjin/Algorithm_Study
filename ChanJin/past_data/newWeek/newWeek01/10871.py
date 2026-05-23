import sys

input = sys.stdin.readline

n, x = map(int, input().split())

myList = list(map(int, input().split()))

for i in myList:
    if x > i:
        print(i, end=' ')


