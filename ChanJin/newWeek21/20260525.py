def solution(citations):
    answer = 0
    len_c = len(citations)
    citations.sort(reverse=True)
    
    for i in range(len_c):
        if citations[i] < i+1:
            return i
    
    return len_c