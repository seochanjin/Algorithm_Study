def solution(n):
    answer = []
    
    triangle = [[0]*(i+1) for i in range(n)]
    
    row, col = -1, 0
    num = 1
    
    directions = 0
    step_count = n
    total = n*(n+1)//2
    
    while num <= total:
        for _ in range(step_count):
            if num > total:
                break
            if directions == 0:
                row += 1
            elif directions == 1:
                col += 1
            else:
                row -= 1
                col -= 1
            triangle[row][col] = num
            num += 1
        directions = (directions + 1) % 3
        step_count -= 1
        
    for r in triangle:
        answer.extend(r)
    
    return answer