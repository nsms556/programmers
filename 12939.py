# 1115 연습문제 > 최댓갑과 최솟값
# https://programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    nums = list(map(int, s.split()))

    return '{} {}'.format(min(nums), max(nums))

s = '1 2 3 4'
print(solution(s))

s = '-1 -2 -3 -4'
print(solution(s))

s = '-1 -1'
print(solution(s))