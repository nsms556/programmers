# 연습문제 > 올바른 괄호
# https://programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    answer = True

    stack = []
    for c in s :
        if c == '(' :
            stack.append(c)
        else :
            if len(stack) < 1 :
                answer = False
            else :
                stack.pop()

    if len(stack) > 0 :
        answer = False

    return answer

s = "()()"
print(solution(s))

s = "(())()"
print(solution(s))

s = ")()("
print(solution(s))

s = "(()("
print(solution(s))
