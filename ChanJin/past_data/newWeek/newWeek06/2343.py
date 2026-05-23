import sys

input = sys.stdin.readline

n, m = map(int, input().split())
study = list(map(int, input().split()))

start = max(study)
end = sum(study)

result = end

while start <= end:
    mid = (start + end) // 2

    count = 1
    currentSum = 0
    for s in study:
        if currentSum + s > mid:
            count += 1
            currentSum = s
        else:
            currentSum += s

    if count <= m:
        result = mid

    else:
        start = mid + 1

print(result)
