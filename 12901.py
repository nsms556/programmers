# 1022 2016년
# https://programmers.co.kr/learn/courses/30/lessons/12901

def solution(a, b):
    weekday = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    d = sum(month[:(a-1)]) + b

    answer = weekday[d % 7]
    return answer

a, b = 1, 1
print(solution(a,b))

a, b = 5, 24
print(solution(a,b))