# 1101 월간 코드 챌린지 시즌1 두 개 뽑아서 더하기
# https://programmers.co.kr/learn/courses/30/lessons/68644

from itertools import combinations

def solution(numbers):
    answer = set()

    for i in combinations(numbers, 2) :
        answer.add(sum(i))

    return sorted(answer)

numbers = [2,1,3,4,1]
print(solution(numbers))

numbers = [5,0,2,7]
print(solution(numbers))