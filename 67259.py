# 2020 카카오 인턴십 > 경주로 건설
# https://programmers.co.kr/learn/courses/30/lessons/67259

from collections import deque

def replace_2d(arr, x1, y1, x2, y2, repl) :
    for y in range(y1, y2) :
        arr[y][x1:x2] = repl[y-y1]

def print_2d(arr) :
    for r in arr :
        print(r)

def solution(board):
    answer = 0

    n = len(board)

    for i in range(n) :
        for j in range(n) :
            if board[i][j] == 0 :
                board[i][j] = [float('inf')] * 4

    board[0][0] = [0,0,0,0]

    cost_board = [[1 for _ in range(n+2)] for _ in range(n+2)]
    replace_2d(cost_board, 1, 1, n+1, n+1, board)

    start = (1,1)
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    queue = deque()
    queue.append((1, 1, -500, -1))

    while queue :
        y, x, cost, prev_dir = queue.popleft()
        
        for i, d in enumerate(dirs) :
            ny = y + d[0]
            nx = x + d[1]

            if cost_board[ny][nx] != 1 :
                if prev_dir == i :
                    new_cost = cost + 100
                else :
                    new_cost = cost + 600

                if new_cost < cost_board[ny][nx][i] :
                    cost_board[ny][nx][i] = new_cost
                    queue.append((ny, nx, new_cost, i))
                    
    print_2d(cost_board)

    answer = min(cost_board[n][n])

    return answer


board = [[0,0,0],[0,0,0],[0,0,0]]
print(solution(board))

board = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
print(solution(board))

board = [[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]
print(solution(board))

board = [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]
print(solution(board))

board = [[0, 0, 0, 0, 0, 0, 0, 0],
         [1, 0, 1, 1, 1, 1, 1, 0],
         [1, 0, 0, 1, 0, 0, 0, 0], 
         [1, 1, 0, 0, 0, 1, 1, 1], 
         [1, 1, 1, 1, 0, 0, 0, 0], 
         [1, 1, 1, 1, 1, 1, 1, 0], 
         [1, 1, 1, 1, 1, 1, 1, 0], 
         [1, 1, 1, 1, 1, 1, 1, 0]]
print(solution(board))