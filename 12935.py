# 1018
# https://programmers.co.kr/learn/courses/30/lessons/12935

def solution(arr):
    m = min(arr)
    answer = [i for i in arr if i != m]

    if len(answer) == 0 :
        answer = [-1]

    return answer

arr = [4,3,2,1]
print(solution(arr))

arr = [10]
print(solution(arr))
