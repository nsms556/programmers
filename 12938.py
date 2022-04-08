# 연습문제 > 최고의 집합
# https://programmers.co.kr/learn/courses/30/lessons/12938

def solution(n, s):
    answer = []
    
    while n and s // n :
        e = s // n
        answer.append(e)
        s -= e
        n -= 1

    if not answer :
        answer = [-1]

    return answer

n, s = 2, 9
print(solution(n, s))

n, s = 2, 1
print(solution(n, s))

n, s = 2, 8
print(solution(n, s))

n, s = 3, 8
print(solution(n, s))

n, s = 3, 2
print(solution(n, s))

'''
1, 1
1
1, 2
2

2, 2
2 // 2 + 1,1

2, 9
9//2 + 1, (9-9//2)

3, 9
9//3 + 2, 6
9//3 + 6//2 + 1, 3

1 1 7   7
1 2 6   12
1 3 5   15
1 4 4   16
2 2 5   20
2 3 4   24
3 3 3   27

4, 12
1 1 1 9 9
1 1 2 8 16
1 1 3 7 21
1 1 4 6 24
1 1 5 5 25
1 2 2 7 28
1 2 3 6 36
1 2 4 5 40
1 3 3 5 45
1 3 4 4 48
2 2 2 6 48
2 2 3 5 60
2 2 4 4 64
2 3 3 4 72
3 3 3 3 81
'''