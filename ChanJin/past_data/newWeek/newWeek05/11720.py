import sys
input = sys.stdin.readline

n = int(input())
num = input().strip()
total_sum = 0

for i in range(len(num)):
    total_sum += int(num[i])

print(total_sum)