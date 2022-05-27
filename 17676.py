# 2018 KAKAO BLIND RECRUITMENT > [1차] 추석 트래픽
# https://programmers.co.kr/learn/courses/30/lessons/17676

import datetime as dt

def solution(lines):
    answer = 0
    preset = 0.001

    p_times = []
    for l in lines :
        ymd, hms, process = l[:-1].split()

        end_time = dt.datetime.strptime(f'{ymd} {hms}', '%Y-%m-%d %H:%M:%S.%f')
        process = float(process) - preset

        start_time = end_time - dt.timedelta(seconds=process)

        p_times.append([start_time, end_time])

    p_times.sort()

    '''for i in p_times :
        print(str(i[0]), str(i[1]))'''

    for _, s in p_times :
        e = s + dt.timedelta(seconds=1)

        cnt = 0
        for period in p_times :
            if s <= period[0] < e or s <= period[1] < e or (period[0] <= s and period[1] >= e) :
                cnt += 1

        answer = max(answer, cnt)

    return answer

lines = [
"2016-09-15 01:00:04.001 2.0s",
"2016-09-15 01:00:07.000 2s"
]
print(solution(lines)) # 1

lines = [
"2016-09-15 01:00:04.002 2.0s",
"2016-09-15 01:00:07.000 2s"
]
print(solution(lines)) # 2

lines = [
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]
print(solution(lines)) # 7
