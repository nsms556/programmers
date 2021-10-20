# 1020 문자열 내림차순으로 배치하기
# https://programmers.co.kr/learn/courses/30/lessons/12917

def solution(s):
    answer = sorted(list(s), reverse=True)
    return ''.join(answer)

s = 'Zbcdefg'
print(solution(s))