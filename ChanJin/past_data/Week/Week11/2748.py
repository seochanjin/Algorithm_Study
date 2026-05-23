import sys
input = sys.stdin.readline

a = []
a.append(0)
a.append(1)

n = int(input())

for i in range(n - 1):
    a.append(a[i] + a[i+1])

print(a[n])
