import sys
input = sys.stdin.readline

n = int(input())
papers = []

for _ in range(n):
    w, h =map(int, input().split())
    papers.append(sorted([w,h], reverse=True))

papers.sort(reverse = True)

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if papers[i][1] <= papers[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
