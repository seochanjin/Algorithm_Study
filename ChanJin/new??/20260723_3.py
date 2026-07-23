def trans(num,n):
    if num == 0:
        return '0'
    
    digits = '0123456789ABCDEF'
    answer = []
    
    while num > 0:
        t = num % n
        answer.append(digits[t])
        num = num // n
    
    answer.reverse()
    return ''.join(answer)
    

def solution(n, t, m, p):
    answer = ''
    long_str = ''
    for i in range(t*m):
        long_str += trans(i, n)
        
    answer = long_str[p-1::m][:t]
    
    
    return answer