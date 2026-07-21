def solution(dirs):
    move = {"U": (0,1), "D": (0,-1), "R": (1,0), "L": (-1,0)}
    
    x, y = 0, 0
    visited_roads = set()
    
    for d in dirs:
        dx, dy = move[d]
        nx, ny = x + dx, y + dy
        
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            road = tuple(sorted([(x,y), (nx,ny)]))
            
            visited_roads.add(road)
            
            x, y = nx, ny
    
    return len(visited_roads)