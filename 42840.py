# 1103 완전탐색 모의고사
# https://programmers.co.kr/learn/courses/30/lessons/42840

from math import ceil

def extend(origin, length) :
    extended = origin * ceil(length / len(origin))
    return extended[:length]

def score(submit, answer) :
    correct = 0

    for i,j in zip(submit, answer) :
        if i == j :
            correct += 1

    return correct

def solution(answers):
    answer = []

    p1 = extend([1,2,3,4,5], len(answers))
    p2 = extend([2,1,2,3,2,4,2,5], len(answers))
    p3 = extend([3,3,1,1,2,2,4,4,5,5], len(answers))

    answer = [score(i, answers) for i in [p1, p2, p3]]

    return [i+1 for i, j in enumerate(answer) if j == max(answer)]

answers = [1,2,3,4,5]
print(solution(answers))

answers = [1,3,2,4,2]
print(solution(answers))