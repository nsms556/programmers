# 1101 위클리 챌린지 최소직사각형
# https://programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    widths = []
    heights = []
    for w, h in sizes :
        if h > w :
            w, h, = h, w

        widths.append(w)
        heights.append(h)
    
    return max(widths) * max(heights)

sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
print(solution(sizes))

sizes = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
print(solution(sizes))

sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
print(solution(sizes))
