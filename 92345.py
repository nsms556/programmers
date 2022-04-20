# 2022 KAKAO BLIND RECRUITMENT > 사라지는 발판
# https://programmers.co.kr/learn/courses/30/lessons/92345
# min - MAX ?
# https://welog.tistory.com/431

def is_avail(board, point) :
    y, x = point

    h = len(board)
    w = len(board[0])

    avail = True
    if x < 0 or x >= w or y < 0 or y >= h or board[y][x] == 0 :
        avail = False
    
    return avail

def find_avail(board, loc) :
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    nexts = []
    for d in directions :
        l = tuple(map(sum, zip(loc, d)))
        if is_avail(board, l) :
            nexts.append(l)

    return nexts

def turn_a(board, aloc, bloc, turn) :
    y, x = aloc

    if board[y][x] == 0 :
        return False, turn
    
    flag = False
    wins = []
    loses = []

    for new_a in find_avail(board, aloc) :
        new_board = [row[:] for row in board]
        new_board[y][x] = 0

        win, new_turn = turn_b(new_board, new_a, bloc, turn+1)

        if win == False :
            wins.append(new_turn)
        else :
            loses.append(new_turn)
        flag = True

    if flag :
        if wins :
            return True, min(wins)
        else :
            return False, max(loses)
    else :
        return False, turn

def turn_b(board, aloc, bloc, turn) :
    y, x = bloc

    if board[y][x] == 0 :
        return False, turn
    
    flag = False
    wins = []
    loses = []

    for new_b in find_avail(board, bloc) :
        new_board = [row[:] for row in board]
        new_board[y][x] = 0

        win, new_turn = turn_a(new_board, aloc, new_b, turn+1)

        if win == False :
            wins.append(new_turn)
        else :
            loses.append(new_turn)
        flag = True

    if flag :
        if wins :
            return True, min(wins)
        else :
            return False, max(loses)
    else :
        return False, turn

def solution(board, aloc, bloc):
    _, answer = turn_a(board, aloc, bloc, 0)

    return answer

board, aloc, bloc = [[1, 1, 1], [1, 1, 1], [1, 1, 1]], [1, 0], [1, 2]
print(solution(board, aloc, bloc))

board, aloc, bloc = [[1, 1, 1], [1, 0, 1], [1, 1, 1]], [1, 0], [1, 2]
print(solution(board, aloc, bloc))

board, aloc, bloc = [[1, 1, 1, 1, 1]], [0, 0], [0, 4]
print(solution(board, aloc, bloc))

board, aloc, bloc = [[1]], [0, 0], [0, 0]
print(solution(board, aloc, bloc))
