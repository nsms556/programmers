# 1105 월간 코드 챌린지 시즌1 내적
# https://programmers.co.kr/learn/courses/30/lessons/70128

def solution(a, b):
    answer = 0

    for i,j in zip(a,b) :
        answer += i * j

    return answer

def product(i) :
    return i[0] * i[1]

def solution(a, b):
    answer = sum(map(product, zip(a,b)))
    return answer

a, b = [1,2,3,4], [-3,-1,0,2]
print(solution(a, b))

a, b = [-1,0,1], [1,0,-1]
print(solution(a, b))
