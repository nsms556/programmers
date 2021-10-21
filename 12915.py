# 1021 문자열 내 마음대로 정렬하기
# https://programmers.co.kr/learn/courses/30/lessons/12915

def solution(strings, n):
    strings = sorted(strings)
    return sorted(strings, key=lambda x : x[n])

strings, n = ['sun', 'bed', 'car'], 1
print(solution(strings, n))

strings, n = ['abce', 'abcd', 'cdx'], 2
print(solution(strings, n))