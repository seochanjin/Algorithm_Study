import sys

input = sys.stdin.readline

k = int(input())
print(k)
ps = []

for i in range(k):
    a = int(input())
    if a != 0:
        ps.append(a)
        print(ps)
    else:
        if len(ps) != 0:
            ps.pop()
            print(ps)

print(sum(ps))