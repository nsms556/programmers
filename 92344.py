# 2022 KAKAO BLIND RECRUITMENT > 파괴되지 않은 건물
# https://programmers.co.kr/learn/courses/30/lessons/92344
# https://tech.kakao.com/2022/01/14/2022-kakao-recruitment-round-1/

from itertools import accumulate

def vertical(board) :
    return list(map(list, zip(*board)))

def solution(board, skill):
    answer = 0

    h = len(board)
    w = len(board[0])

    delta = [[0 for _ in range(w+1)] for _ in range(h+1)]

    for t, r1, c1, r2, c2, degree in skill :
        r2, c2 = r2+1, c2+1
        if t == 1 :
            delta[r1][c1] += -degree
            delta[r2][c2] += -degree
            delta[r1][c2] += degree
            delta[r2][c1] += degree
        else :
            delta[r1][c1] += degree
            delta[r2][c2] += degree
            delta[r1][c2] += -degree
            delta[r2][c1] += -degree

    for i in range(h) :
        delta[i] = list(accumulate(delta[i]))

    delta = vertical(delta)

    for i in range(h) :
        delta[i] = list(accumulate(delta[i]))

    delta = vertical(delta)

    delta = [r[:-1] for r in delta[:-1]]

    for b, d in zip(board, delta) :
        for bb, dd in zip(b, d) :
            if bb + dd > 0 :
                answer += 1

    return answer

board, skill = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
print(solution(board, skill))

board, skill = [[1,2,3],[4,5,6],[7,8,9]], [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]
print(solution(board, skill))
 