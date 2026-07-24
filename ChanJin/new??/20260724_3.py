def trans(num, k):
    if num == 0:
        return '0'
    answer = []
    
    while num > 0:
        t = num%k
        answer.append(str(t))
        num = num//k
    answer.reverse()
    return ''.join(answer)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    
    n = trans(n, k)
    parts = n.split('0')
    for part in parts:
        if part == '':
            continue
        if is_prime(int(part)):
            answer += 1
    
    return answer