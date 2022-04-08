# 연습문제 > 2 x n 타일링
# https://programmers.co.kr/learn/courses/30/lessons/12900

from collections import deque

def solution(n):
    tile = deque([0, 1, 2])

    for i in range(3, n+1) :
        tile.append((tile[i-1] + tile[i-2]) % 1000000007)

    return tile[-1]

n = 4
print(solution(n))

n = 5
print(solution(n))


'''
0   
1   1
2   s0+2, s1+1
3   2+1, 1+2
4   3+1, 2+2
5   4+1, 3+2

'''