import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    
    while scoville[0] < K and len(scoville) > 1:
        answer += 1
        a1 = heapq.heappop(scoville)
        a2 = heapq.heappop(scoville)
        result = a1 + (a2 * 2)
        heapq.heappush(scoville, result)
    
    if scoville[0] < K:
        return -1
    
    return answer