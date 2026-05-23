import sys
input = sys.stdin.readline

def sol():
    n = int(input())
    tel = [input().strip() for _ in range(n)]

    tel.sort()

    for i in range(len(tel) - 1):
        if tel[i+1].startswith(tel[i]):
            print("NO")
            return
    
    print("YES")

t = int(input())
for _ in range(t):
    sol()
