def solution(s):
    words = s.split(" ")
    answer = []
    
    for word in words:
        if word:
            answer.append(word[0].upper() + word[1:].lower())
        else:
            answer.append(word)
        
    return ' '.join(answer)
