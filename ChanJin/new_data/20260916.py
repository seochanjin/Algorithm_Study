def solution(want, number, discount):
    answer = 0

    dis_day = {}
    want_dic = {}
    cut = 0

    for i in range(len(want)):
        want_dic[want[i]] = number[i]

    for i in range(10):
        item = discount[i]
        dis_day[item] = dis_day.get(item, 0) + 1

    if dis_day == want_dic:
        answer += 1

    for i in range(10, len(discount)):
        add_item = discount[i]
        remove_item = discount[i-10]

        dis_day[add_item] = dis_day.get(add_item, 0) + 1

        dis_day[remove_item] -= 1

        if dis_day[remove_item] == 0:
            del dis_day[remove_item]

        if dis_day == want_dic:
            answer += 1

    return answer