# 1101 월간 코드 챌린지 시즌2 약수의 개수와 덧셈
# https://programmers.co.kr/learn/courses/30/lessons/77884

from math import sqrt

def solution(left, right):
    answer = 0

    for i in range(left, right+1) :
        if sqrt(i) % 1 == 0 :
            answer -= i
        else :
            answer += i

    return answer

def solution(left, right):
    answer = [i if sqrt(i) % 1 != 0 else i * -1 for i in range(left,right+1)]
        
    return sum(answer)

left, right = 13, 17
print(solution(left, right))

left, right = 24,27
print(solution(left, right))