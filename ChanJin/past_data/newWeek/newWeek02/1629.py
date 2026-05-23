import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

def solve(a, b):
    if b==1:
        return a%c
    m = b//2
    half = solve(a,m)%c

    if b%2 == 0:
        return (half*half)%c
    else:
        return ((a%c)*half*half)%c

print(solve(a,b))

#######################################################

import sys
input=sys.stdin.readline

a, b, c = map(int, input().split())
print(pow(a,b,c))