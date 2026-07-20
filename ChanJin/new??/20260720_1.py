from collections import deque

def solution(cacheSize, cities):
    
    if cacheSize == 0:
        return len(cities) * 5
    
    answer = 0
    
    queue = deque([])
    
    for city in cities:
        city = city.lower()
        if city in queue:
            answer += 1
            queue.remove(city)
            queue.append(city)
        else:
            if len(queue) >= cacheSize:
                queue.popleft()
            queue.append(city)
            answer += 5
    
    return answer