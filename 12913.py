# 1117 연습문제 > 땅따먹기
# https://programmers.co.kr/learn/courses/30/lessons/12913

def solution(land):
    for i in range(1, len(land)) :
        for j in range(4) :
            land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])

    return max(land[-1])

land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
print(solution(land))

land = [[1,2,3,5],[5,6,7,100],[4,3,2,1]]
print(solution(land))

land = [[1,1,1,1],[2,2,2,3],[3,3,3,6], [4,4,4,7]]
print(solution(land))
