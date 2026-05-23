# 의상 (난이도 Lv.2)

from collections import defaultdict


def solution(clothes):
    answer = 0

    clothes_map = defaultdict(int)

    for name, kind in clothes:
        clothes_map[kind] += 1

    answer = 1

    for count in clothes_map.values():
        answer = answer * (count + 1)

    return answer - 1