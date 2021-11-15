# 1115 연습문제 > 피보나치 수
# https://programmers.co.kr/learn/courses/30/lessons/12945

def solution(n):
    a = 0
    b = 1

    for _ in range(n) :
        a, b = b, (a + b) % 1234567 

    return a

n = 3
print(solution(n))

n = 5
print(solution(n))