import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

result = []

def dfs(index, re, plus, minus, mul, div):
    if index == n:
        result.append(re)
        return
    
    if plus > 0:
        dfs(index+1, re+nums[index], plus-1, minus,mul,div)
    if minus > 0:
        dfs(index+1, re-nums[index], plus, minus-1, mul, div)
    if mul>0:
        dfs(index+1, re*nums[index], plus, minus, mul-1, div)
    if div>0:
        if re < 0:
            dfs(index+1, -(-re//nums[index]), plus, minus, mul, div-1)
        else:
            dfs(index+1, re//nums[index], plus, minus, mul, div-1)

dfs(1, nums[0], plus, minus, mul, div)

print(max(result))
print(min(result))