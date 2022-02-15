# 2020 KAKAO BLIND RECRUITMENT > 괄호 변환
# https://programmers.co.kr/learn/courses/30/lessons/60058

from collections import deque

def is_correct(s) :
    stack = deque()

    for c in s :
        if c == '(' :
            stack.append(c)
        else :
            if not stack :
                return False
            else :
                stack.pop()
    
    if stack :
        return False

    return True

def divide(s) :
    p = deque(s)

    u = ''
    left = 0
    right = 0

    while not (left == right and left > 0) :
        c = p.popleft()
        u += c
        if c == '(' :
            left += 1
        elif c == ')' :
            right += 1

    return u, ''.join(p)

def solution(p) :
    if is_correct(p) or p == '' :
        return p
    else :
        u, v = divide(p)

        if is_correct(u) :
            return u + solution(v)
        else :
            answer = '(' + solution(v) + ')'
    
            for c in u[1:-1] :
                if c == '(' :
                    answer += ')'
                else :
                    answer += '('
    
            return answer
    
p = "(()())()"
print(solution(p))

p = ")("
print(solution(p))

p = "()))((()"
print(solution(p))