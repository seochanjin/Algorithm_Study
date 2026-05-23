import sys

input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

dp = [0] * n
dp[0] = a[0][0]

for i in range(1, n):
    for j in range(i , -1, -1):
        if j == i:
            dp[j] = dp[j-1] + a[i][j]
        elif j == 0:
            dp[j] = dp[j] + a[i][j]
        else:
            dp[j] = max(dp[j-1], dp[j]) + a[i][j]

print(max(dp))