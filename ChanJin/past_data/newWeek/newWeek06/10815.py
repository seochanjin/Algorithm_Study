import sys
input = sys.stdin.readline

n = int(input())
card = list(map(int,input().split()))
m = int(input())
check = list(map(int, input().split()))

card.sort()

def search(array, target, start, end):
    while start <= end:
        mid = (start + end) //2
        if array[mid] == target:
            return 1
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid +1
    return 0

result = []
for target in check:
    result.append(search(card, target, 0, n - 1))

print(*result)