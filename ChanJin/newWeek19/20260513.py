def solution1(arr): # 시간 오래걸림
    max_arr = arr[-1]
    answer = max_arr

    while True:
        value = True

        for i in arr:
            if answer % i != 0:
                value = False
                break
        
        if value:
            return answer
    
        answer += max_arr



# gemini가 추천해준 최소공배수 공식을 사용하여 풀 수 있는 방법
from math import gcd # 최대공약수를 구하는 함수

def solution(arr):
    answer = arr[0]
    
    for i in range(1, len(arr)):
        # 두 수 (a, b)의 최소공배수 = (a * b) / 최대공약수
        # 이 공식을 사용하면 루프 한 번에 바로 계산됩니다.
        answer = (answer * arr[i]) // gcd(answer, arr[i])
        
    return answer