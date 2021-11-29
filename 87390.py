# 월간 코드 챌린지 시즌3 > n^2 배열 자르기
# https://programmers.co.kr/learn/courses/30/lessons/87390

def solution(n, left, right):
    left_r, left_c = divmod(left, n)
    right_r, right_c = divmod(right, n)

    arr = [[max(i, j) for i in range(1, n+1)] for j in range(left_r+1, right_r+2)]

    answer = []
    for a in arr :
        answer.extend(a)

    left = left_c
    right = (right_r - left_r) * n + right_c

    return answer[left:right+1]

def solution(n, left, right) :
    answer = []

    for i in range(left, right+1) :
        answer.append(max(i//n, i%n)+1)

    return answer

n, left, right = 3, 2, 5
print(solution(n, left, right))
'''
left_r,c = 0, 2
right_r,c = 1, 2

1 2 | 3
2 2 3 |
3 3 3

'''
n, left, right = 4, 7, 14
print(solution(n, left, right))
'''
start_r = 1
start_c = 3
end_r = 3
end_c = 2

1 2 3 4
2 2 3 | 4
3 3 3 4
4 4 4 | 4
'''