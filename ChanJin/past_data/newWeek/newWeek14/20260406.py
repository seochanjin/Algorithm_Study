remove_zero = 0

def solution(s):
    trans_cnt = 0
    
    while s != "1":
        trans_cnt += 1
        
        s = change_bn(count_zero(s))
        
    return [trans_cnt, remove_zero]

def change_bn(num):
    bn = ""
    while num > 0:
        value = num%2
        if value == 0:
            bn = "0" + bn
        else:
            bn = "1" + bn
        num = num // 2
    return bn
        

def count_zero(x):
    result = 0
    global remove_zero
    
    for i in x:
        if i == "0":
            remove_zero += 1
            continue
        else:
            result+=1
            
    return result
    