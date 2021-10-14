# 문자열 다루기 기본
# https://programmers.co.kr/learn/courses/30/lessons/12918

def solution(s):
    l = len(s)
    n = s.isnumeric()
    
    return (l == 4 or l == 6) and n