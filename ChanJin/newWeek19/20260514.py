def solution(elements):
    answer = 0
    n = len(elements)
    extended_elements = elements * 2
    u_sum = set()
    
    for length in range(1, n + 1):
        for i in range(n):
            sub_sum = sum(extended_elements[i : i + length])
            u_sum.add(sub_sum)
    
    return len(u_sum)


# gemini 버전
def solution(elements):
    n = len(elements)
    extended = elements * 2
    u_sum = set()

    for length in range(1, n + 1):
        # 첫 번째 윈도우의 합을 미리 구함
        current_sum = sum(extended[0:length])
        u_sum.add(current_sum)
        
        # 슬라이딩: 한 칸씩 옆으로 밀면서 '앞은 빼고 뒤는 더하기'
        for i in range(1, n):
            current_sum = current_sum - extended[i-1] + extended[i + length - 1]
            u_sum.add(current_sum)
            
    return len(u_sum)