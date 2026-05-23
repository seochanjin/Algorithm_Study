import sys

input = sys.stdin.readline

t = int(input())

a=[]
for i in range(t):
    cnt = 0
    a = input().strip()

    if a[0] == ')':
        print("NO")
        continue

    for i in range(len(a)):
        if a[i] == '(':
            cnt += 1
        else:
            cnt -= 1
            if (cnt < 0):
                break
        
    if cnt == 0:
        print("YES")
    else:
        print("NO")