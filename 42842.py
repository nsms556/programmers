# 완전탐색 > 카펫
# https://programmers.co.kr/learn/courses/30/lessons/42842

def holy_water(i) :
    ret = []

    for d in range(1, int(i ** 0.5)+1) :
        if i % d == 0 :
            ret.append((d, i // d))

    return ret

def solution(brown, yellow):
    for h, w in holy_water(yellow) :
        if (h + w) * 2 + 4 == brown :
            return [w+2, h+2]

from math import sqrt

def solution(brown, yellow) :
    b = (brown+4)//2
    c = brown + yellow

    h = (b - sqrt(b**2 - 4*c)) // 2
    w = (b + sqrt(b**2 - 4*c)) // 2

    return [w, h]

brown, yellow = 10, 2
print(solution(brown, yellow))

brown, yellow = 8, 1
print(solution(brown, yellow))

brown, yellow = 24, 24
print(solution(brown, yellow))
