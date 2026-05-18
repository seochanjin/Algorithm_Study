def solution(want, number, discount):
    
    answer = 0
    want_base = {}
    
    for w, n in zip(want, number):
        want_base[w] = n
    
    for i in range(len(discount) - 9):
        check_dict = want_base.copy()
        
        for j in range(i, i + 10):
            item = discount[j]
            
            if item in check_dict:
                check_dict[item] -= 1
                
        if all(val <= 0 for val in check_dict.values()):
            answer += 1
    
    return answer