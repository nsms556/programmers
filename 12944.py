# 1014 평균 구하기
# https://programmers.co.kr/learn/courses/30/lessons/12944

def solution(arr):
    return sum(arr) / len(arr)

arr = [1,2,3,4]
print(solution(arr))

arr = [5,5]
print(solution(arr))