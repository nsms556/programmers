# 월간 코드 챌린지 시즌3 > 빛의 경로 사이클
# https://programmers.co.kr/learn/courses/30/lessons/86052

from itertools import product


def change_absolute_dir(prev_dir, dir) :
    l = {'U':'L', 'L':'D', 'D':'R', 'R':'U'}
    r = {'U':'R', 'L':'U', 'D':'L', 'R':'D'}

    if dir == 'L' :
        return l[prev_dir]
    elif dir == 'R' :
        return r[prev_dir]
    else :
        return prev_dir

def solution(grid):
    answer = []

    grid = list(map(list, grid))
    shots = [[[0,0,0,0] for _ in row] for row in grid]

    ab_dirs = {'U':0, 'L':1, 'D':2, 'R':3}

    w = len(grid[0])
    h = len(grid)

    def next_point(x, y, prev_dir) :
        d = {'U':(0, -1), 'L':(-1, 0), 'D':(0, 1), 'R':(1, 0)}
        next_dir = change_absolute_dir(prev_dir, grid[y][x])
        
        next_x = x + d[next_dir][0]
        next_y = y + d[next_dir][1]

        if next_x < 0 :
            next_x = w - 1
        elif next_x == w :
            next_x = 0
        
        if next_y < 0 :
            next_y = h - 1
        elif next_y == h :
            next_y = 0
        
        return (next_x, next_y, next_dir)
    
    for x, y in product(range(w), range(h)) :
        for d in ab_dirs :
            route = []

            while shots[y][x][ab_dirs[d]] == 0 :
                route.append((x, y, d))
                shots[y][x][ab_dirs[d]] = 1

                x, y, d = next_point(x, y, d)

            if route :
                answer.append(len(route))

    return sorted(answer)

grid = ["SL","LR"]
print(solution(grid))

grid = ["S"]
print(solution(grid))

grid = ["R","R"]
print(solution(grid))

grid = ["SS","SS"]
print(solution(grid))