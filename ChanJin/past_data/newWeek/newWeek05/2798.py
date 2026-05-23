import sys

input = sys.stdin.readline

n, m = map(int, input().split())
card = list(map(int, input().split()))

total = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            curSum = card[i] + card[j] + card[k]

            if curSum <= m:
                total = max(total, curSum)

print(total)
