import sys

input = sys.stdin.readline
n = int(input())
room = []
for i in range(n):
    room.append(list(map(int, input().split())))
room.sort(key=lambda x: (x[1], x[0]))
cnt = 1
min = room[0][1]
for i in range(1, n):
    if min <= room[i][0]:
        min = room[i][1]
        cnt += 1
print(cnt)
