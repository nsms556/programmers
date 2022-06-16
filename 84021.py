# 위클리 챌린지 > 퍼즐 조각 채우기
# https://programmers.co.kr/learn/courses/30/lessons/84021

from collections import deque


def rotate_clockwise(arr) :
    return list(map(list, zip(*arr[::-1])))

def replace_2d(arr, x1, y1, x2, y2, repl) :
    for y in range(y1, y2+1) :
        arr[y][x1:x2+1] = repl[y - y1]

def print_2d(arr) :
    print('[{}'.format(arr[0]))
    for r in arr[1:-1] :
        print(' {}'.format(r))
    print(' {}]'.format(arr[-1]))

def extract_piece(arr, start_point) :
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    piece_points = [start_point, ]

    stack = deque()
    stack.append(start_point)

    while stack :
        point = stack.pop()
        
        for d in dirs :
            new_y = point[0] + d[0]
            new_x = point[1] + d[1]

            if (new_y, new_x) not in piece_points :
                if arr[new_y][new_x] == 0 :
                    piece_points.append((new_y, new_x))
                    stack.append((new_y, new_x))

    return piece_points
    
def find_blank(arr) :
    n = len(arr) - 2
    pieces_loc = []
    visited = []

    for i in range(1, n+1) :
        for j in range(1, n+1) :
            if (i, j) in visited :
                continue

            visited.append((i, j))

            if arr[i][j] == 1 :
                continue
            else :
                pieces_x, pieces_y = [], []
                for point in extract_piece(arr, (i, j)) :
                    visited.append(point)
                    pieces_x.append(point[1])
                    pieces_y.append(point[0])

                pieces_loc.append([(min(pieces_y), min(pieces_x)), (max(pieces_y), max(pieces_x))])

    return pieces_loc

def slice_2d(arr, p1, p2) :
    y1, x1 = p1
    y2, x2 = p2

    return [row[x1:x2+1] for row in arr[y1:y2+1]]

def piece_size(piece) :
    h = len(piece)
    w = len(piece[0])

    return h * w - sum(map(sum, piece))

def solution(game_board, table):
    answer = 0
    n = len(game_board)

    new_board = [[1 for _ in range(n+2)] for _ in range(n+2)]
    replace_2d(new_board, 1, 1, n, n, game_board)

    table = [[1-i for i in row] for row in table]
    new_table = [[1 for _ in range(n+2)] for _ in range(n+2)]
    replace_2d(new_table, 1, 1, n, n, table)

    blanks = find_blank(new_board)
    pieces = find_blank(new_table)

    for b_p1, b_p2 in blanks :
        blk_shape = slice_2d(new_board, b_p1, b_p2)
        
        flag = False
        for p_p1, p_p2 in pieces :
            p_shape = slice_2d(new_table, p_p1, p_p2)

            for _ in range(4) :
                p_shape = rotate_clockwise(p_shape)
                if blk_shape == p_shape :
                    pieces.remove([p_p1, p_p2])
                    flag = True
                    break

            if flag :
                break

        if flag :
            answer += piece_size(blk_shape)

    return answer

game_board, table = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]], [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]
print(solution(game_board, table))

game_board, table = [[0,0,0],[1,1,0],[1,1,1]], [[1,1,1],[1,0,0],[0,0,0]]
print(solution(game_board, table))
