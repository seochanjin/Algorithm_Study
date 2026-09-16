def solution(sequence, k):
    answer = []
    n = len(sequence)
    
    current_sum = 0
    left, right = 0, 0
    min_len = float('inf')
    
    while right < n:
        current_sum += sequence[right]
        
        while current_sum > k:
            current_sum -= sequence[left]
            left += 1
            
        if current_sum == k:
            current_length = right - left
            if current_length < min_len:
                min_len = current_length
                answer = [left, right]
                
        right += 1
        
    return answer