# 1018 자연수 뒤집어 배열로 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12932

def solution(n) :
    return list(map(int, reversed(str(n))))

n = 12345
print(solution(n))