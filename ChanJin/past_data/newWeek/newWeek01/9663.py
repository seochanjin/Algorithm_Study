import sys

input = sys.stdin.readline

n = int(input())

pos = [0] * n
flag_a = [False] * n
flag_b = [False] * (2 * n - 1)
flag_c = [False] * (2 * n - 1)

count = 0

def queen(depth):
    if depth == n:
        global count
        count += 1
        return

    for i in range(n):
        if (not flag_a[i]) and (not flag_b[depth+i]) and (not flag_c[depth-i+n-1]):
            flag_a[i] = flag_b[depth+i] = flag_c[depth-i+n-1] = True
            pos[depth] = i
            queen(depth+1)
            flag_a[i] = flag_b[depth+i] = flag_c[depth-i+n-1] = False


queen(0)
print(count)

