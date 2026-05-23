import sys

input = sys.stdin.readline

n = int(input())
x = []

for _ in range(n):
    command = input().split()

    if command[0] == "push":
        x.append(command[1])

    elif command[0] == "pop":
        if len(x) == 0:
            print(-1)
            continue
        top = x.pop()
        print(top)

    elif command[0] == "size":
        print(len(x))

    elif command[0] == "empty":
        if len(x) == 0:
            print(1)
        else:
            print(0)

    elif command[0] == "top":
        if len(x) == 0:
            print(-1)
            continue
        print(x[-1])
