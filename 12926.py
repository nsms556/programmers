# 1018 시저 암호
# https://programmers.co.kr/learn/courses/30/lessons/12926

def solution(s, n):
    answer = ''
    upper = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    lower = list('abcdefghijklmnopqrstuvwxyz')

    for i, c in enumerate(list(s)) :
        if c in upper :
            answer += upper[(upper.index(c)+n) % 26] 
        elif c in lower :
            answer += lower[(lower.index(c)+n) % 26]
        else :
            answer += c

    return str(answer)

s, n = 'AB', 1
print(solution(s, n))

s, n = 'z', 1
print(solution(s, n))

s, n = 'a B z', 4
print(solution(s, n))