# 1115 연습문제 > JadenCase 문자열 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    return ' '.join(map(lambda x : x.capitalize(), s.split(' ')))

s = "3people unFollowed me"
print(solution(s))

s = "for the last week"
print(solution(s))

s = "abc   def  ghij klm"
print(solution(s))
