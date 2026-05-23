import sys
input = sys.stdin.readline

leftStack = list(input().strip())
rightStack = []
n = int(input())

for _ in range(n):
    command = input().split()

    if command[0] == 'L':
        if leftStack:
            rightStack.append(leftStack.pop())

    elif command[0] == 'D':
        if rightStack:
            leftStack.append(rightStack.pop())

    elif command[0] == 'B':
        if leftStack:
            leftStack.pop()

    elif command[0] == 'P':
        leftStack.append(command[1])

print("".join(leftStack + rightStack[::-1]))