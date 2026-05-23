def solution(n):
    answer = 0
    compare_num = change_bn(n).count("1")
    n = n + 1
    while compare_num != change_bn(n).count("1"):
        n = n + 1
    
    return n

def change_bn(number):
    bn = ""
    while number > 0:
        value = number%2
        if value == 1:
            bn = "1" + bn
        else:
            bn = "0" + bn
        number = number//2
    return bn
        