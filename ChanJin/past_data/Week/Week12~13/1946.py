import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
    test_count = int(input())
    testcase = []
    for i in range(test_count):
        testcase.append(list(map(int, input().split())))
    testcase.sort()
    min = testcase[0][1]
    cnt = 1
    for i in range(1, test_count):

        if min >= testcase[i][1]:
            min = testcase[i][1]
            cnt += 1
    print(cnt)
