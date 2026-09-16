from collections import Counter

def solution(weights):
    answer = 0
    count = Counter(weights)
    unique_weights = sorted(count.keys())
    
    for w1 in unique_weights:
        answer += count[w1] * (count[w1] - 1) // 2
        
        for w2 in [w1 * 4 / 3, w1 * 3 / 2, w1 * 2]:
            if w2 in count:
                answer += count[w1] * count[w2]
                

    return answer