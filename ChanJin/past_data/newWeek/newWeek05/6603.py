import sys
input = sys.stdin.readline

def dfs(idx, depth):
    if depth == 6:
        print(*result)
        return

    for i in range(idx, k):
        result.append(s[i])
        dfs(i+1, depth+1)
        result.pop()

while True:
    data = list(map(int, input().split()))
    if data[0] == 0:
        break

    k = data[0]
    s = data[1:]
    result = []

    dfs(0, 0)
    print()