def solution(n, words):
    used_words = set()
    used_words.add(words[0])
    
    for i in range(1, len(words)):
        if words[i][0] != words[i-1][-1] or words[i] in used_words:
            player_number = (i%n) + 1
            turn = (i//n) + 1
            return [player_number, turn]

        used_words.add(words[i])

    return [0,0]