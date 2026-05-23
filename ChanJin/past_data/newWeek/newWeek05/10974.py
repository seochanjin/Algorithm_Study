import sys
input = sys.stdin.readline

n = int(input())

visited = [False] * (n + 1)
result = []

def dfs(depth):
    if depth == n:
        print(*result)
        return

    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            result.append(i)

            dfs(depth + 1)

            result.pop()
            visited[i] = False

dfs(0)



