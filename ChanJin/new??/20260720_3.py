def solution(s):
    answer = []
    
    raw_tuples = s[2:-2].split("},{")
    
    raw_tuples.sort(key=len)
    
    for group in raw_tuples:
        numbers = list(map(int, group.split(",")))
        
        for num in numbers:
            if num not in answer:
                answer.append(num)
    
    return answer