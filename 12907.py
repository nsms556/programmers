# 연습문제 > 거스름돈
# https://programmers.co.kr/learn/courses/30/lessons/12907
# https://programmers.co.kr/questions/25161

def solution(n, money):
    changes = [1] + [0 for _ in range(n)]

    for coin in money :
        for i in range(1, n+1) :
            if i >= coin :
                changes[i] += changes[i-coin] % 1000000007

    return changes[-1]

n, money = 5, [1,2,5]
print(solution(n, money))
