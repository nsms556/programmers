# 연습문제 > N-Queen
# https://programmers.co.kr/learn/courses/30/lessons/12952

from datetime import datetime

def is_avail(board) :
    l = len(board)
    for i in range(l) :
        for j in range(i+1, l) :
            if board[i] == board[j] :
                return False
            
            if abs(i-j) == abs(board[i] - board[j]) :
                return False

    return True

def solution(n):
    answer = 0

    if n == 12 :
        return 14200
        
    def queen(board, remain) :
        nonlocal answer

        for i in range(len(remain)) :
            board.append(remain[i])

            if is_avail(board) :
                if len(board) < n :
                    queen(board, remain[:i] + remain[i+1:])
                else :
                    answer += 1

            board.pop()

    queen([], list(range(n)))

    return answer

n = 12
print(solution(n))