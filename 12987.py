# Summer/Winter Coding(~2018) > 숫자 게임
# https://programmers.co.kr/learn/courses/30/lessons/12987

from collections import deque

def solution(A, B):
    answer = 0

    A.sort(reverse=True)
    B = deque(sorted(B, reverse=True))

    for enemy in A :
        if B[0] > enemy :
            answer += 1
            B.popleft()

    return answer

a, b = [5,1,3,7], [2,2,6,8]
print(solution(a, b))

a, b = [2,2,2,2], [1,1,1,1]
print(solution(a, b))