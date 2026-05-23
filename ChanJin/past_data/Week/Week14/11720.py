import sys

input = sys.stdin.readline
n = int(input())
a = input()
b = []
sum = 0
for i in range(n):
    sum += int(a[i])

print(sum)
