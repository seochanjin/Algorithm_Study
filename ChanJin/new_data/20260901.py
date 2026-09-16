def solution(n):
    answer = ''
    digit = {0: '1', 1: '2', 2:'4'}
    stack = []
    
    while n > 0:
        n -= 1
        remainder = n%3
        stack.append(digit[remainder])
        n = n//3
        
    stack.reverse()
    answer = answer.join(stack)
    
    return answer