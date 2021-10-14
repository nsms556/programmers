# 1013 행렬의 덧셈
# https://programmers.co.kr/learn/courses/30/lessons/12950
'''
def solution(arr1, arr2):
    answer = []

    h, w = len(arr1), len(arr1[0])

    for y in range(h) :
        subarray = []
        for x in range(w) :
            subarray.append(arr1[y][x] + arr2[y][x])
        answer.append(subarray)

    return answer
'''

def solution(arr1, arr2):
    answer = [[a+b for a,b in zip(sub1, sub2)] for sub1, sub2 in zip(arr1, arr2)]

    return answer

arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]
print(solution(arr1, arr2))

arr1 = [[1],[2]]
arr2 = [[3],[4]]
print(solution(arr1, arr2))