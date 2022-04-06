# Summer/Winter Coding(2019) > 멀쩡한 사각형
# https://programmers.co.kr/learn/courses/30/lessons/62048
# https://leedakyeong.tistory.com/entry/프로그래머스-멀쩡한-사각형-in-python

from math import gcd

def solution(w,h):

    g = gcd(w, h)

    return w * h - (w + h - g)
'''
w, h = 8, 12
print(solution(w, h))

w, h = 7, 4
print(solution(w, h))

w, h = 4, 7
print(solution(w, h))

w, h = 100000000, 1000000000
print(solution(w, h))

w, h = 2, 3
print(solution(w, h))
'''
w, h = 99999999, 99999998
print(solution(w, h))


'''
7 x 4 -> 2 + 3 + 3 + 2

'''