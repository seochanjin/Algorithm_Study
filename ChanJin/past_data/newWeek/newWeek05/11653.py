import sys

input = sys.stdin.readline

n = int(input())


def sol(n):
    if n == 1:
        return
    i = 2
    while i * i <= n:
        if n % i == 0:
            print(i)
            n //= i
        else:
            i += 1

    if n > 1:
        print(n)


sol(n)
