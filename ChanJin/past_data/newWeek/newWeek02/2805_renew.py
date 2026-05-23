import sys

input = sys.stdin.readline

n, m = map(int, input().split())
tree = list(map(int, input().split()))

start = 0
end = max(tree)
result = 0

while start <= end:
    mid = (start + end) // 2

    total = sum(t - mid for t in tree if t > mid)

    if total >= m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)