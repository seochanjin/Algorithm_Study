# 스택 버전

def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []
    
    for i in range(n):
        while stack and prices[stack[-1]] > prices[i]:
            idx = stack.pop()
            answer[idx] = i - idx
        stack.append(i)
        
    while stack:
        idx = stack.pop()
        answer[idx] = n - 1 - idx
        
    return answer


# 아예 틀림

from collections import deque

def solution(prices):
    answer = []
    
    len_price = len(prices)
    price_que = deque(prices)
    
    for i in range(len_price - 1):
        price = price_que.popleft()
        count = 0
        for pri in price_que:
            if price > pri:
                break
            count += 1
        if count == 0: count += 1
        answer.append(count)
    
    answer.append(0)
    return answer


