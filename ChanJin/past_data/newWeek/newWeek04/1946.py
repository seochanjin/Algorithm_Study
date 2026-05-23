import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    score = [list(map(int, input().split())) for _ in range(n)]
    score.sort()

    minScore = score[0][1]
    cnt = 1
    for j in range(1, n):
        if minScore >= score[j][1]:
            minScore = score[j][1]
            cnt += 1
    print(cnt)