import sys
input = sys.stdin.readline

a = []
k = int(input())

for i in range(k):
    b = int(input())
    if b != 0:
        a.append(b)
    else:
        if len(a) != 0:
            a.pop()

print(sum(a))
