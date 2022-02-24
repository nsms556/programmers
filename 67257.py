# 2020 카카오 인턴십 > 수식 최대화
# https://programmers.co.kr/learn/courses/30/lessons/67257

from itertools import permutations
import re

def in_to_post(expression, op_order) :
    expression = re.findall('[0-9]+|[+*-]', expression)
    
    stack = []
    postfix = []
    for item in  expression :
        if item not in op_order :
            postfix.append(item)
        else :
            if not stack :
                stack.append(item)
            else :
                while stack and op_order[stack[-1]] >= op_order[item] :
                    postfix.append(stack.pop())
                stack.append(item)

    while stack :
        postfix.append(stack.pop())

    return postfix

def calc_post(postfix) :
    stack = []

    for item in postfix :
        if item == '*' :
            op2 = stack.pop()
            stack.append(stack.pop() * op2)
        elif item == '+' :
            op2 = stack.pop()
            stack.append(stack.pop() + op2)
        elif item == '-' :
            op2 = stack.pop()
            stack.append(stack.pop() - op2)
        else :
            stack.append(int(item))

    return stack.pop()

def solution(expression):
    answer = 0

    operators = set(re.findall('[*+-]', expression))
    
    for order in permutations(operators) :
        op_order = {op:i for i, op in enumerate(order)}
        
        score = abs(calc_post(in_to_post(expression, op_order)))
        if score > answer :
            answer = score 

    return answer

def solution(expression):
    operations = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),('-', '*', '+'),('*', '+', '-'),('*', '-', '+')]
    answer = []
    for op in operations:
        a = op[0]
        b = op[1]
        temp_list = []
        for e in expression.split(a):
            temp = [f"({i})" for i in e.split(b)]
            temp_list.append(f'({b.join(temp)})'

        answer.append(abs(eval(a.join(temp_list))))
    return max(answer)

expression = "100-200*300-500+20"
print(solution(expression))
'''
expression = "50*6-3*2"
print(solution(expression))
'''