# 1108 월간 코드 챌린지 시즌3 없는 숫자 더하기
# https://programmers.co.kr/learn/courses/30/lessons/86051

def solution(numbers):
    origin = set([0,1,2,3,4,5,6,7,8,9])
    numbers = set(numbers)

    return sum(origin - numbers)

numbers = [1,2,3,4,6,7,8,0]
print(solution(numbers))

numbers = [5,8,4,0,6,7,9]
print(solution(numbers))