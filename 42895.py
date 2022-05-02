# 동적계획법(Dynamic Programming) > N으로 표현
# https://programmers.co.kr/learn/courses/30/lessons/42895

from itertools import product

def solution(N, number):
    answer = -1

    dp = {i:set() for i in range(1, 9)}

    for i in range(1, 9) :
        dp[i].add(int(str(N) * i))

    for i in range(1, 9) :
        for j in range(1, i) :
            for op1, op2 in product(dp[j], dp[i-j]) :
                dp[i].add(op1 + op2)
                dp[i].add(op1 - op2)
                dp[i].add(op1 * op2)
                if op2 != 0 :
                    dp[i].add(op1 // op2)

        if number in dp[i] :
            answer = i
            break

    return answer

N, number = 5, 12
print(solution(N, number))

N, number = 2, 11
print(solution(N, number))

