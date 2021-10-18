# 1018 정수 제곱근 판별
# https://programmers.co.kr/learn/courses/30/lessons/12934

import math

def solution(n):
    if math.sqrt(n) % 1 == 0 :
        answer = int((math.sqrt(n) + 1) ** 2)
    else :
        answer = -1
        
    return answer

n = 121
print(solution(n))

n = 3
print(solution(n))