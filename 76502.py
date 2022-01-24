# 월간 코드 챌린지 시즌2 > 괄호 회전하기
# https://programmers.co.kr/learn/courses/30/lessons/76502

from collections import deque

def avail(s) :
    stack = deque()

    bracket_pair = {')':'(', '}':'{', ']':'['}

    for c in s :
        if c in '[{(' :
            stack.append(c)
        else :
            if not stack :
                return False

            if not stack[-1] == bracket_pair[c] :
                return False
            else :
                stack.pop()
            
    if stack :
        return False

    return True

def solution(s):
    answer = 0
    
    s = deque(s)
    
    for _ in range(len(s)) :
        s.rotate(1)

        if avail(s) :
            answer += 1

    return answer

s = "[](){}"
print(solution(s))

s = "}]()[{"
print(solution(s))

s = "[)(]"
print(solution(s))

s = "}}}"
print(solution(s))
