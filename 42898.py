# 동적계획법(Dynamic Programming) > 등굣길
# https://programmers.co.kr/learn/courses/30/lessons/42898

def solution(m, n, puddles):
    roadmap = [[0 for _ in range(m+1)] for _ in range(n+1)]

    roadmap[1][1] = 1

    for y in range(1, n+1) :
        for x in range(1, m+1) :
            if [x, y] in puddles or [y, x] == [1, 1]:
                continue

            roadmap[y][x] = (roadmap[y][x-1] + roadmap[y-1][x]) % 1000000007

    answer = roadmap[-1][-1]

    for r in roadmap :
        print(r)

    return answer

m, n, puddles = 4, 3, [[2, 2]]
print(solution(m, n, puddles))