# 월간 코드 챌린지 시즌1 > 쿼드압축 후 개수 세기
# https://programmers.co.kr/learn/courses/30/lessons/68936

import numpy as np

def solution(arr):
    c0, c1 = 0, 0

    def quad(arr) :
        nonlocal c0, c1

        if np.all(arr == 0) :
            c0 += 1
        elif np.all(arr == 1) :
            c1 += 1
        else :
            l = len(arr) // 2

            q1 = arr[:l, l:]
            q2 = arr[:l, :l]
            q3 = arr[l:, :l]
            q4 = arr[l:, l:]

            for i, q in enumerate([q1,q2,q3,q4]) :
                tree = {}
                tree[i] = quad(q)

    quad(np.array(arr))

    return [c0, c1]

arr = [[1,1,0,0],
       [1,0,0,0],
       [1,0,0,1],
       [1,1,1,1]]
print(solution(arr))

arr = [[1,1,1,1,1,1,1,1],
       [0,1,1,1,1,1,1,1],
       [0,0,0,0,1,1,1,1],
       [0,1,0,0,1,1,1,1],
       [0,0,0,0,0,0,1,1],
       [0,0,0,0,0,0,0,1],
       [0,0,0,0,1,0,0,1],
       [0,0,0,0,1,1,1,1]]
print(solution(arr))

arr = [[0, 0],
       [0, 0]]
print(solution(arr))

arr = [[1, 1],
       [1, 1]]
print(solution(arr)) 