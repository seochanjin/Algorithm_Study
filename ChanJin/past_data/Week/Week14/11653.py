import sys

input = sys.stdin.readline

n = int(input())

idx = 2
while n != 1:
    while True:
        if n % idx != 0:
            break
        n = n / idx
        print(idx)
    idx += 1
