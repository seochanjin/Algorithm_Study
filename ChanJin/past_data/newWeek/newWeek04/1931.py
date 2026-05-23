import sys

input = sys.stdin.readline

n = int(input())

info = []
for i in range(n):
    info.append(list(map(int, input().split())))

info.sort(key=lambda x: (x[1], x[0]))

cnt = 1
minTime = info[0][1]
for i in range(1, n):
    if minTime <= info[i][0]:
        minTime = info[i][1]
        cnt += 1

print(cnt)
