def solution(numbers):
    stack = []
    lenNum = len(numbers)
    answer = [-1] * lenNum

    for i in range(lenNum):
        while stack and numbers[stack[-1]] < numbers[i]:
            idx = stack.pop()
            answer[idx] = numbers[i]

        stack.append(i)

    return answer