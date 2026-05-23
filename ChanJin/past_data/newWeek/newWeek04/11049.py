import sys
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]

for term in range(1, n):
    for start in range(n - term):
        end = start + term

        dp[start][end] = float('inf')

        for k in range(start, end):
            cost = dp[start][k] + dp[k+1][end] + (matrix[start][0] * matrix[k][1] * matrix[end][1])

            dp[start][end] = min(dp[start][end], cost)


print(dp[0][n-1])