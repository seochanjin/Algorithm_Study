import sys
input = sys.stdin.readline

n = int(input())
a = [0]
for i in range(n):
    a.append(int(input()))

dp = [0]*(n+1)

dp[1] = a[1]

if n >= 2:
    dp[2] = a[1] + a[2]

if n >= 3:
    dp[3] = max(a[1] + a[3], a[2] + a[3])

for i in range(4, n+1):
    dp[i] = max(dp[i-2] + a[i], dp[i-3] + a[i-1] + a[i])

print(dp[n])