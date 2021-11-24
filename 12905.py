# 연습문제 > 가장 큰 정사각형 찾기
# https://programmers.co.kr/learn/courses/30/lessons/12905

def solution(board):
    for i in range(1, len(board)) :
        for j in range(1, len(board[0])) :
            if board[i][j] != 0 :
                board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1]) + 1

    return max(map(max, board)) ** 2

board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
print(solution(board))

board = [[0,0,1,1],[1,1,1,1]]
print(solution(board))