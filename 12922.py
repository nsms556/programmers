# 1020 수박수박수박수박수박수?
# https://programmers.co.kr/learn/courses/30/lessons/12922

def solution(n):
    answer = '수박' * (n // 2 + 1)
    return answer[:n]

n = 3
print(solution(n))

n = 4
print(solution(n))
