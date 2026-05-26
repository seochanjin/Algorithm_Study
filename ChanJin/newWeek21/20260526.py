from itertools import permutations

def solution(k, dungeons):
    answer = -1
    
    for p in permutations(dungeons, len(dungeons)):
        current_k = k
        count = 0
        
        for min_value, consume_value in p:
            if current_k >= min_value:
                current_k -= consume_value
                count += 1
            else:
                break
                
        answer = max(answer, count)
    
    return answer