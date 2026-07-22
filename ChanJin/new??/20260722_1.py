def solution(word):
    dictionary = []
    vowels = ['A', 'E', 'I', 'O', 'U']
    
    def dfs(current_word):
        if len(current_word) == 5:
            return
        
        for v in vowels:
            next_word = current_word + v
            dictionary.append(next_word)
            dfs(next_word)
    
    dfs("")
    
    return dictionary.index(word) + 1