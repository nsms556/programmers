# 연습문제 > 멀리 뛰기
# https://programmers.co.kr/learn/courses/30/lessons/12914

from collections import deque

def solution(n): 
    jump = deque([0, 1, 2])

    for i in range(3, n+1) :
        jump.append((jump[i-1] + jump[i-2]) % 1234567)

    return jump[n]

n = 4
print(solution(n))

n = 3
print(solution(n))