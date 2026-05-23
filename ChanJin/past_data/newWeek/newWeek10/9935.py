import sys
input = sys.stdin.readline

a = input().strip()
b = input().strip()

lastB = b[-1]
lenB = len(b)

stack = []

for i in a:
    stack.append(i)

    if i == lastB and len(stack) >= lenB:
        if "".join(stack[-lenB:]) == b:
            for _ in range(lenB):
                stack.pop()

if not stack:
    print("FRULA")
else:
    print("".join(stack))