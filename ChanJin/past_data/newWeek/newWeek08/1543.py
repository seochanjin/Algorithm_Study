import sys

input = sys.stdin.readline

doc = input().rstrip()
word = input().rstrip()

answer = 0
index = 0

while index <= len(doc) - len(word):
    if doc[index: index + len(word)] == word:
        answer += 1
        index += len(word)
    else:
        index += 1

print(answer)
