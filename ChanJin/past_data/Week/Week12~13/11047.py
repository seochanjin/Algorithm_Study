import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = []
for i in range(n):
    a.append(int(input()))

cnt = 0

a= a[::-1]

for i in a:
    if i <= k:
        cnt += k//i
        k = k%i
print(cnt)