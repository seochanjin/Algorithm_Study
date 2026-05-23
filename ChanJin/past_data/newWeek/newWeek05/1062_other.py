import sys
from itertools import combinations

input = sys.stdin.readline

n, k = map(int, input().split())

if k < 5:
    print(0)
    exit()
if k == 26:
    print(n)
    exit()

words_bit = []
for _ in range(n):
    word = input().strip()
    bit = 0
    for char in word:
        bit |= (1 << (ord(char) - ord('a')))
    words_bit.append(bit)

essential_chars = ['a','n','t','i','c']
essential_bit = 0
for char in essential_chars:
    essential_bit |= (1<<(ord(char)-ord('a')))

candidates = [1 << i for i in range(26) if not (essential_bit & (1 << i))]

max_result = 0

for combo in combinations(candidates, k-5):
    learned_bit = essential_bit
    for bit in combo:
        learned_bit |= bit

    count = 0
    for word_bit in words_bit:
        if (word_bit & learned_bit) == word_bit:
            count += 1

    max_result = max(max_result, count)

print(max_result)