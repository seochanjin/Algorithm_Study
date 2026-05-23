import sys

input = sys.stdin.readline

k, n = map(int, input().split())
lanCable = list(int(input()) for _ in range(k))

start = 1
end = max(lanCable)
result = 0

while start <= end:
    mid = (start + end) // 2

    total = sum(l//mid for l in lanCable)

    if total >= n:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)