def solution(numbers):
    n = len(numbers)
    answer = [-1] * n
    stack = []

    for i in range(n):
        while stack and numbers[stack[-1]] < numbers[i]:
            idx = stack.pop()
            answer[idx] = numbers[i]
            
        stack.append(i)

    return answer


# 문제를 잘못이해했음
def solution(numbers):
    answer = []
    len_num = len(numbers)
    
    for i in range(len_num-1):
        if numbers[i] <= numbers[i+1]:
            numbers[i] = numbers[i+1]
        else:
            numbers[i] = -1
    
    numbers[len_num-1] = -1
    
    return numbers