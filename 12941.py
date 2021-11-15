# 1115 연습문제 > 최솟값 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12941

def solution(A,B):
    answer = 0

    for i, j in zip(sorted(A), sorted(B, reverse=True)) :
        answer += i * j
        
    return answer

A, B = [1,4,2], [5,4,4]
print(solution(A, B))

A, B = [1,2], [3,4]
print(solution(A, B))