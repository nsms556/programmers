# 1115 연습문제 > 행렬의 곱셈
# https://programmers.co.kr/learn/courses/30/lessons/12949

import numpy as np

def solution(arr1, arr2):
    answer = np.dot(np.array(arr1), np.array(arr2)).tolist()
    return answer

arr1, arr2 = [[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]
print(solution(arr1, arr2))

arr1, arr2 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
print(solution(arr1, arr2))