import sys

input = sys.stdin.readline

n = int(input())
length = list(map(int, input().split()))
gas = list(map(int, input().split()))

total_cost = 0
min_price = gas[0]

for i in range(n - 1):
    if gas[i] < min_price:
        min_price = gas[i]

    total_cost += min_price * length[i]

print(total_cost)