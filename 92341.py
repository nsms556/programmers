# 2022 KAKAO BLIND RECRUITMENT > 주차 요금 계산
# https://programmers.co.kr/learn/courses/30/lessons/92341

from math import ceil

def solution(fees, records):
    answer = []

    total_time = {}
    parking_in = {}

    for r in records :
        time, plate, io = r.split()
        
        time = list(map(int, time.split(':')))
        time = time[0] * 60 + time[1]

        if io == 'IN' :
            parking_in[plate] = time

        else :
            total_time[plate] = total_time.get(plate, 0) + (time - parking_in.pop(plate))

    for plate, intime in parking_in.items() :
        total_time[plate] = total_time.get(plate, 0) + (23 * 60 + 59 - intime)
    
    for _, parking in sorted(total_time.items(), key=lambda x : x[0]) :
        fee = fees[1]

        if parking > fees[0] :
            parking -= fees[0]
            fee += ceil(parking / fees[2]) * fees[3]

        answer.append(fee)

    return answer

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees, records))

fees = [120, 0, 60, 591]
records = ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]
print(solution(fees, records))

fees = [1, 461, 1, 10]
records = ["00:00 1234 IN"]
print(solution(fees, records))
