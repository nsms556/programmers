# 1020 문자열 내 p와 y의 개수
# https://programmers.co.kr/learn/courses/30/lessons/12916

def solution(s):
    s = list(s.lower())

    p = s.count('p')
    y = s.count('y')
    
    if p == y :
        answer = True
    else :
        answer = False 

    return answer

s = 'pPoooyY'
print(solution(s))

s = 'Pyy'
print(solution(s))
