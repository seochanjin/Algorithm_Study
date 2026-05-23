import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

m = 1000000003

dp = [[0]*(k+1) for _ in range(n + 1)]

for i in range(n+1):
    dp[i][0] = 1
    dp[i][1] = i

for i in range(2, n+1):
    for j in range(2, k+1):
        dp[i][j] = (dp[i-1][j] + dp[i-2][j-1]) % m

ans = (dp[n-3][k-1] + dp[n-1][k]) % m
print(ans)