import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

a = []
for i in range(1, n+1):
    a.append(i)

queue = deque(a)
result = []

while queue:
    for _ in range(k-1):
        queue.append(queue.popleft())

    result.append(str(queue.popleft()))

print("<"+", ".join(result)+">")
