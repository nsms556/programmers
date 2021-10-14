# 1013 x만큼 간격이 있는 n개의 숫자
# https://programmers.co.kr/learn/courses/30/lessons/12954

def solution(x, n):
    answer = []
    origin_x = x

    answer = [x + (origin_x * i) for i in range(n)]

    return answer

x=2
n=5
print(solution(x, n))

x=4
n=3
print(solution(x, n))

x=-4
n=2
print(solution(x, n))
