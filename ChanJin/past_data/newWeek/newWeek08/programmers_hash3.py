# 귤고르기 (난이도 Lv2)

from collections import defaultdict

def solution(k, tangerine):
    answer = 0

    counts = defaultdict(int)
    for t in tangerine:
        counts[t] += 1

    sorted_counts = sorted(counts.values(), reverse=True)

    total = 0
    for i in sorted_counts:
        total += i
        answer += 1
        if total >= k:
            break

    return answer