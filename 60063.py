# 2020 KAKAO BLIND RECRUITMENT > 블록 이동하기
# https://programmers.co.kr/learn/courses/30/lessons/60063
# https://velog.io/@tjdud0123/블록-이동하기-2020-카카오-공채-python

from collections import deque    

def replace_2d(array, repl, x1, y1, x2) :
    y = y1
    
    for row in repl :
        array[y][x1:x2] = row
        y += 1

    return array

def solution(board):
    answer = 0

    n = len(board)
    new_board = [[1 for _ in range(n+2)] for _ in range(n+2)]
    board = replace_2d(new_board, board, 1, 1, n+1)
    dirs = [(0,1), (-1, 0), (0,-1), (1,0)]

    def check_point(p) :
        y, x = p

        return board[y][x] == 0

    def move(p1, p2) :
        avails = []

        for dy, dx in dirs :
            new_p1 = (p1[0]+dy, p1[1]+dx)
            new_p2 = (p2[0]+dy, p2[1]+dx)

            if check_point(new_p1) and check_point(new_p2) :
                avails.append((new_p1, new_p2))

        if p1[0] == p2[0] :
            for dy in [-1, 1] :
                new_p1 = (p2[0]+dy, p2[1])
                new_p2 = (p1[0]+dy, p1[1])

                if check_point(new_p1) and check_point(new_p2) :
                    avails.append((p1, new_p2))
                    avails.append((p2, new_p1))
        else :
            for dx in [-1, 1] :
                new_p1 = (p2[0], p2[1]+dx)
                new_p2 = (p1[0], p1[1]+dx)

                if check_point(new_p1) and check_point(new_p2) :
                    avails.append((p1, new_p2))
                    avails.append((p2, new_p1))

        return avails

    start = ((1,1), (1,2), 0)

    queue = deque()
    visited = set()

    queue.append(start)
    visited.add((start[:2]))

    while queue :
        p1, p2, answer = queue.popleft()

        if p1 == (n, n) or p2 == (n, n) :
            break

        for new_points in move(p1, p2) :
            if new_points not in visited :
                queue.append((*new_points, answer + 1))
                visited.add(new_points)

    return answer

board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
print(solution(board))