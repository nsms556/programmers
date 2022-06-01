# 연습문제 > 최적의 행렬 곱셈
# https://programmers.co.kr/learn/courses/30/lessons/12942
# https://huiyu.tistory.com/entry/DP-%EC%97%B0%EC%87%84%ED%96%89%EB%A0%AC-%EC%B5%9C%EC%86%8C%EA%B3%B1%EC%85%88-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98

def solution(matrix_sizes):
    answer = 0

    l = len(matrix_sizes)
    
    dp = [[float('inf') for _ in range(l)] for _ in range(l)]

    for diag in range(l) :
        for i in range(l-diag) :
            j = i + diag
            if i == j :
                dp[i][j] = 0
            else :
                for k in range(i, j) :
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + (matrix_sizes[i][0] * matrix_sizes[k][1] * matrix_sizes[j][1]))

    answer = dp[0][-1]

    return answer

matrix_sizes = [[5,3],[3,10],[10,6]]    # 180 + 90
print(solution(matrix_sizes))

matrix_sizes = [[5,1],[1,5],[5,3]]       # 15 + 15
print(solution(matrix_sizes))

matrix_sizes = [[10,5],[5,3],[3,6],[6,8],[8,1]]     # 48 + 18 + 15 + 50
print(solution(matrix_sizes))
