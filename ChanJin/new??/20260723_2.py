# 성공
def solution(land):
    dp = land[0][:]    
    
    for i in range(1, len(land)):
        max1 = max2 = -1
        max1_idx = -1
        for k in range(4):
            if dp[k] > max1:
                max2 = max1
                max1 = dp[k]
                max1_idx = k
            elif dp[k] > max2:
                max2 = dp[k]
                
        row = land[i]
        new_dp = [0,0,0,0]
        for j in range(4):
            best = max2 if j == max1_idx else max1
            new_dp[j] = row[j] + best
            
        dp = new_dp
        
    return max(dp)


# 시간 초과
def solution(land):
    dp = land[0][:]    
    
    for i in range(1, len(land)):
        new_dp = [0] * 4
        for j in range(4):
            new_dp[j] = land[i][j] + max(dp[k] for k in range(4) if k != j)
        dp = new_dp
        
    return max(dp)

