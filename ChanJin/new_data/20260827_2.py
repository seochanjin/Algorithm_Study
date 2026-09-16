from collections import defaultdict
import heapq

def solution(N, road, K):
    answer = 0
    
    graph = defaultdict(list)
    for a, b, c in road:
        graph[a].append((b,c))
        graph[b].append((a,c))
        
    INF = float('inf')
    dist = [INF] * (N + 1)
    dist[1] = 0

    heap = [(0, 1)]
    
    while heap:
        cur_dist,cur_node = heapq.heappop(heap)       
        if cur_dist > dist[cur_node]:
            continue
            
        for next_node, weight in graph[cur_node]:
            new_dist = cur_dist + weight
            if new_dist < dist[next_node]:
                dist[next_node] = new_dist
                heapq.heappush(heap, (new_dist, next_node))
        
    answer = sum(1 for d in dist[1:] if d <= K)
    

    return answer