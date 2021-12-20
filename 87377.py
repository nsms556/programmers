# 위클리 챌린지 > 교점에 별 만들기
# https://programmers.co.kr/learn/courses/30/lessons/87377

from itertools import combinations

def solve(line1, line2) :
    a, b, e = line1
    c, d, f = line2

    if a*d - b*c == 0 :
        return 0.1, 0.1
    else :
        return (b*f - e*d) / (a*d - b*c), (e*c - a*f) / (a*d - b*c)

def convert_point(new_origin, point) :
    x, y = point

    x += -new_origin[0]
    y = -y + new_origin[1]

    return int(y), int(x)

def solution(line):
    cross_x = []
    cross_y = []

    for i, j in combinations(line, 2) :
        x, y = solve(i, j)
        if x.is_integer() and y.is_integer() :
            cross_x.append(x)
            cross_y.append(y)

    w, h = int(max(cross_x) - min(cross_x) + 1), int(max(cross_y) - min(cross_y) + 1)
    new_origin = min(cross_x), max(cross_y)

    plot = [['.' for _ in range(w)] for _ in range(h)]

    for i, j in zip(cross_x, cross_y) :
        y, x = convert_point(new_origin, (i, j))
        plot[y][x] = '*'

    plot = list(map(''.join, plot))

    return plot

line = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]
print(solution(line))
'''
[-0.0, -4.0, 4.0, 4.0, -4.0] [4.0, -4.0, -4.0, 1.0, 1.0]
9 x 9, -4,4 -> 0, 0 | 0, 0 -> 4, -4 -> 4,4
-4, -4 -> 8, 0
4, -4 -> 8, 8
-4, 1 -> 3, 0
'''

line = [[0, 1, -1], [1, 0, -1], [1, 0, 1]]
print(solution(line))
'''
[1.0, -1.0] [1.0, 1.0]
3 x 1 -1,1 -> 0,0
1, 1 -> 0, 2
-1, 1 -> 0, 0
'''


line = [[1, -1, 0], [2, -1, 0]]
print(solution(line))

line = [[1, -1, 0], [2, -1, 0], [4, -1, 0]]
print(solution(line))

