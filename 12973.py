# 2017 팁스타운 > 짝지어 제거하기
# https://programmers.co.kr/learn/courses/30/lessons/12973

from collections import deque

def solution(s):
    stack = deque()

    for c in s :
        if not stack :
            stack.append(c)
        else :
            if c == stack[-1] :
                stack.pop()
            else :
                stack.append(c)

    if stack :
        answer = 0
    else :
        answer = 1 

    return answer
 
s = 'baabaa'
print(solution(s))

s = 'cdcd'
print(solution(s))

s = 'adbccbad'
print(solution(s))