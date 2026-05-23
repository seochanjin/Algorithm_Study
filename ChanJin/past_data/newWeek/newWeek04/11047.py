import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coinValue=[]
for i in range(n):
    coinValue.append(int(input()))

cnt = 0

# for i in range(n):
#     if k//coinValue[n-1-i] >= 1:
#         cnt += k // coinValue[n - 1 - i]
#         k -= coinValue[n-1-i] * (k//coinValue[n-1-i])
#     else:
#         continue

for coin in reversed(coinValue):
    cnt += k//coin
    k %= coin

print(cnt)