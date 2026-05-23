import sys

input = sys.stdin.readline

n = int(input())
mixList = list(input().strip())
totalSum = 0
temp = ''

for i in range(n):
    if '0' <= mixList[i] <= '9':
        temp += mixList[i]
    else:
        if temp != '':
            totalSum += int(temp)
            temp = ''

if temp != '':
    totalSum += int(temp)

print(totalSum)