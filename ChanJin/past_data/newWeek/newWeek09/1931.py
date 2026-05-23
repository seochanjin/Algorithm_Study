import sys
input = sys.stdin.readline

n = int(input())

a = []
for i in range(n):
    a.append(list(map(int, input().split())))

a.sort(key=lambda x: (x[1], x[0]))

cnt = 1
min_time = a[0][1]
for i in range(1, n):
    if min_time <= a[i][0]:
        min_time = a[i][1]
        cnt+=1
print(cnt)