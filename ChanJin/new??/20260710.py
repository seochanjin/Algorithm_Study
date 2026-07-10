from collections import Counter

def solution(topping):
    answer = 0
    
    right_dict = Counter(topping)
    left_set = set()
    
    for t in topping:
        left_set.add(t)
        right_dict[t] -= 1
        
        if right_dict[t] == 0:
            del right_dict[t]
            
        if len(left_set) == len(right_dict):
            answer += 1
    
    return answer
    