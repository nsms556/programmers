# 2018 KAKAO BLIND RECRUITMENT > [1차] 셔틀버스
# https://programmers.co.kr/learn/courses/30/lessons/17678

from collections import deque

def calc_minute(time_str) :
    h, m = map(int, time_str.split(':'))

    return h * 60 + m

def to_str(time_min) :
    h, m = divmod(time_min, 60)

    return '{:02d}:{:02d}'.format(h, m)

def solution(n, t, m, timetable):
    timetable = deque(sorted(map(calc_minute, timetable)))
    
    bus_t = calc_minute('09:00')

    buses = [bus_t]
    for _ in range(n-1) :
        bus_t += t
        buses.append(bus_t)
    
    for i, bus in enumerate(buses) :
        ride = 0
        if i == len(buses)-1 :
            while timetable and timetable[0] <= bus and ride < m-1 :
                timetable.popleft()
                ride += 1

            if timetable :
                answer = min(bus, timetable[0]-1)
            else :
                answer = bus
        else :
            while timetable[0] <= bus and ride < m :
                timetable.popleft()
                ride += 1
            else :
                ride = 0

    answer = to_str(answer)

    return answer

n, t, m, timetable = 1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]
print(solution(n, t, m, timetable))

n, t, m, timetable = 2, 10, 2, ["09:10", "09:09", "08:00"]
print(solution(n, t, m, timetable))

n, t, m, timetable = 2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]
print(solution(n, t, m, timetable))

n, t, m, timetable = 1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]
print(solution(n, t, m, timetable))

n, t, m, timetable = 1, 1, 1, ["23:59"]
print(solution(n, t, m, timetable))

n, t, m, timetable = 10, 60, 45, ["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]
print(solution(n, t, m, timetable))
