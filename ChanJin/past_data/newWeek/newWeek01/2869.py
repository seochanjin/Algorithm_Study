import sys

input = sys.stdin.readline
a, b, v = map(int, input().split())

# count = 0
# currentHeight = 0
dairyHeight = a - b
days = (v-a)//dairyHeight

if (v-a)%dairyHeight != 0:
    days += 1

print(days + 1)

#시간 초과
# while True:
#     currentHeight+=dairyHeight
#     count += 1
#     if currentHeight + a >= v:
#         break
#
# print(count+1)