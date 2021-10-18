# 1018 자릿수더하기
# https://programmers.co.kr/learn/courses/30/lessons/12931

def solution(n) :
    return sum(map(int, str(n)))

n = 123
print(solution(n))

n = 987
print(solution(n))