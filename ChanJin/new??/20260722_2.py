from collections import Counter

def solution(str1, str2):
    
    list1 = [str1[i:i+2].upper() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    list2 = [str2[i:i+2].upper() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    
    count1 = Counter(list1)
    count2 = Counter(list2)
    
    intersection = count1 & count2
    union = count1 | count2
    
    sum_inter = sum(intersection.values())
    sum_union = sum(union.values())
    
    if sum_union == 0:
        return 65536
    
    return int((sum_inter/sum_union)*65536)



def solution(str1, str2):
    list1 = [str1[i:i+2].upper() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    list2 = [str2[i:i+2].upper() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    
    list2_copy = list2.copy()
    inter_count = 0
    
    for item in list1:
        if item in list2_copy:
            inter_count += 1
            list2_copy.remove(item)
            
    union_count = len(list1) + len(list2) - inter_count
    
    if union_count == 0:
        return 65536
        
    return int((inter_count / union_count) * 65536)