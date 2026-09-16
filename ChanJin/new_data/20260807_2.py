from collections import deque, defaultdict

def count_nodes(start, graph, blocked_edge):
    visited = {start}
    queue = deque([start])
    
    while queue:
        node = queue.popleft() 
        for neighbor in graph[node]:
            if (node, neighbor) == blocked_edge or (neighbor, node) == blocked_edge:
                continue
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return len(visited)

def solution(n, wires):
    graph = defaultdict(list)
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    min_diff = n 
    
    for v1, v2 in wires:
        count = count_nodes(v1, graph, (v1, v2))
        diff = abs(count - (n - count))
        min_diff = min(min_diff, diff)
    
    return min_diff