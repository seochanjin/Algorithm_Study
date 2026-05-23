# 가장 큰 수 (난이도 Lv 2)

def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    answer = ''.join(numbers)
    answer = str(int(answer))
    return answer