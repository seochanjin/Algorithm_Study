import sys

input = sys.stdin.readline

n = int(input())

a = input()
a = a.lower()

check = ""
total = 0


for i in range(n):
    if "0" <= a[i] <= "9":
        check += a[i]
    else:
        if check:
            total += int(check)
            check = ""

if check:
    total += int(check)


print(total)
