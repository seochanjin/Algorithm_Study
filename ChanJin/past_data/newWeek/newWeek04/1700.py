import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))

plug = []
cnt = 0

for i in range(k):
    current = a[i]

    if current in plug:
        continue

    if len(plug) < n:
        plug.append(current)
        continue

    last_used_idx = -1
    target = -1

    for p in plug:

        if p in a[i+1:]:
            idx = a.index(p, i + 1)
        else:
            idx = float('inf')

        if idx > last_used_idx:
            last_used_idx = idx
            target = p

    plug.remove(target)
    plug.append(current)
    cnt += 1

print(cnt)
