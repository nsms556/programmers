# 월간 코드 챌린지 시즌1 > 삼각 달팽이
# https://programmers.co.kr/learn/courses/30/lessons/68645


def solution(n):
    answer = [[0] * i for i in range(1,n+1)]

    row, col = -1, 0
    direction = {'d':(1, 0), 'r':(0, 1), 'u':(-1, -1)}
    i = 1

    d = 'd'
    for repeat in range(n, 0, -1) :
        for _ in range(repeat) :
            row += direction[d][0]
            col += direction[d][1]
            
            answer[row][col] = i
            i += 1

        if d == 'd' :
            d = 'r'
        elif d == 'r' :
            d = 'u'
        elif d == 'u' :
            d = 'd'

    return sum(answer, [])

n = 1
print(solution(n))

n = 2
print(solution(n))

n = 3
print(solution(n))

n = 4
print(solution(n))

n = 5
print(solution(n))

n = 6
print(solution(n))

'''
[1] ... [n ~ 2n-1]

[3]
1 2 3 4 5 6
1 2 6 3 4 5

[4]
1 2 3 4 5  6 7 8 9 10
1 2 9 3 10 8 4 5 6 7

[5]
1 2 3  4 5  6  7 8  9  10 11 12 13 14 15
1 2 12 3 13 11 4 14 15 10 5  6  7  8  9

[6]
1 2 3  4 5  6  7 8  9  10 11 12 13 14 15 16 17 18 19 20 21
1 2 15 3 16 14 4 17 21 13 5  18 19 20 12 6  7  8  9  10 11
'''