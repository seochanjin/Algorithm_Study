# 주차 요금 계산 (난이도 Lv2)

import math
from collections import defaultdict


def solution(fees, records):
    answer = []

    base_time, base_fee, unit_time, unit_fee = fees

    def get_min(time_str):
        h, m = map(int, time_str.split(':'))
        return (h * 60) + m

    parking = {}
    total_times = defaultdict(int)

    for r in records:
        time, car_id, status = r.split()
        curr_min = get_min(time)

        if status == "IN":
            parking[car_id] = curr_min
        else:
            in_min = parking.pop(car_id)
            total_times[car_id] += (curr_min - in_min)

    last_min = get_min("23:59")
    for car_id, in_min in parking.items():
        total_times[car_id] += (last_min - in_min)

    sorted_cars = sorted(total_times.items())

    for car_id, time in sorted_cars:
        if time <= base_time:
            fee = base_fee
        else:
            fee = base_fee + math.ceil((time - base_time) / unit_time) * unit_fee
        answer.append(fee)

    return answer