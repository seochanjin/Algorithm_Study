import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    total = 0
    ps = input().strip()

    for i in ps:
        if i == "(":
            total += 1
        else:
            total -= 1
            if total < 0:
                break
    if total == 0:
        print("YES")
    else:
        print("NO")
