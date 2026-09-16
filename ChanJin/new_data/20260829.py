from collections import deque

def solution(players, m, k):
    answer = 0
    active = deque()
    
    for i in range(24):
        while active and active[0] <= i:
            active.popleft()
            
        need = players[i] // m
        
        current = len(active)
        if need > current:
            add = need - current
            answer += add
            for _ in range(add):
                active.append(i + k)
    
    return answer