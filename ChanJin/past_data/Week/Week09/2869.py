import sys

# input = sys.stdin.readline

a, b, v = map(int ,input().split())


n = ((v - a) + (a - b - 1)) // (a - b) + 1

print(n)


# 낮에는 a 만큼 올라가고 밤에 b만큼 내려간다. 높이는 v
# (v - a)(a - b) 
# 어쨋든 낮에 올라가야 하니까 v-a를 a-b를 n으로 곱하면 되는거잖아?
# 틀리네 