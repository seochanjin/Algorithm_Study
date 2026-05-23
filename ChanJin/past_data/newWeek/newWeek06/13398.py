import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

dp = [[0]*2 for _ in range(n)]

dp[0][0] = a[0]
dp[0][1] = a[0]

ans = a[0]

for i in range(1, n):
    dp[i][0] = max(dp[i-1][0] + a[i], a[i])

    dp[i][1] = max(dp[i-1][0], dp[i-1][1]+a[i])

    ans = max(ans, dp[i][0], dp[i][1])

print(ans)