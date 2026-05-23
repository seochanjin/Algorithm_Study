import sys
from collections import deque

input = sys.stdin.readline

queue = deque()

n = int(input())

for _ in range(n):
    command = input().split()
    if command[0] == "push":
        queue.append(command[1])

    elif command[0] == "pop":
        if len(queue) == 0:
            print(-1)
            continue
        b = queue.popleft()
        print(b)

    elif command[0] == "size":
        print(len(queue))

    elif command[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    elif command[0] == "front":
        if len(queue) == 0:
            print(-1)
            continue
        print(queue[0])

    elif command[0] == "back":
        if len(queue) == 0:
            print(-1)
            continue
        print(queue[-1])
