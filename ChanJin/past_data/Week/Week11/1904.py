import sys

input = sys.stdin.readline

n  = int(input())

a = []
a.append(1)
a.append(2)

for i in range(n-1):
    a.append((a[i] + a[i+1])%15746)


print(a[n-1])