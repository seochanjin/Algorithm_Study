from math import gcd
from functools import reduce

def get_divisors(num):
    divisors = []
    i = 1
    while i * i <= num:
        if num % i == 0:
            divisors.append(i)
            if i != num // i:
                divisors.append(num // i)
        i += 1
    return divisors

def solution(arrayA, arrayB):
    answer = 0
    
    gcd_a = reduce(gcd, arrayA)
    gcd_b = reduce(gcd, arrayB)
    
    for d in get_divisors(gcd_a):
        if all(b%d != 0 for b in arrayB):
            answer = max(answer, d)
            
    for d in get_divisors(gcd_b):
        if all(b%d != 0 for b in arrayA):
            answer = max(answer, d)
    
    return answer