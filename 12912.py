# 1021 두 정수 사이의 합
# https://programmers.co.kr/learn/courses/30/lessons/12912

def solution(a, b):
    if a > b :
        a, b = b, a

    return sum(range(a, b+1))

def solution(a, b) :
    if a > b :
        a, b = b, a

    return int(b * (b + 1) / 2) - int(a * (a - 1) / 2)

a, b = 3, 5
print(solution(a, b))

a, b = 3, 3
print(solution(a, b))

a, b = 5, 3
print(solution(a, b))

a, b = 1, 10
print(solution(a, b))

a, b = -10, -1
print(solution(a, b))
