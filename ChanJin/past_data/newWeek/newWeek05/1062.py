import sys

input = sys.stdin.readline

n, k = map(int, input().split())


def count_readable_words(learned):
    count = 0
    for word in words:
        can_read = True
        for char in word:
            if not learned[ord(char) - ord('a')]:
                can_read = False
                break
        if can_read:
            count += 1
    return count


def dfs(idx, cnt):
    global max_result

    if cnt == k:
        max_result = max(max_result, count_readable_words(learned))
        return

    if idx == 26:
        return

    if not learned[idx]:
        learned[idx] = True
        dfs(idx + 1, cnt + 1)

        learned[idx] = False
        dfs(idx + 1, cnt)
    else:
        dfs(idx + 1, cnt)


if k < 5:
    print(0)
    exit()

words = []
for _ in range(n):
    words.append(input().strip()[4:-4])

learned = [False] * 26
for char in ['a', 'n', 't', 'i', 'c']:
    learned[ord(char) - ord('a')] = True

max_result = 0

dfs(0, 5)

print(max_result)

####################################################################################################
