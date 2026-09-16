def solution(storey):
    def helper(storey):
        if storey == 0:
            return 0
    
        value = storey % 10
        remain = storey // 10
        
        if value > 5:
            return (10 - value) + helper(remain + 1)
        elif value < 5:
            return value + helper(remain)
        else: 
            opt1 = value + helper(remain)          
            opt2 = (10 - value) + helper(remain + 1)  
            return min(opt1, opt2)

    return helper(storey)