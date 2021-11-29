# Summer/Winter Coding(~2018) > 방문 길이
# https://programmers.co.kr/learn/courses/30/lessons/49994

def solution(dirs):
    route = set()
    x, y = 0, 0

    for d in dirs :
        if d == 'U' and y < 5 :
            route.add((x, y, d))
            y += 1
            route.add((x, y, 'D'))
        elif d == 'L' and x > -5 :
            route.add((x, y, d))
            x -= 1
            route.add((x, y, 'R'))
        elif d == 'D' and y > -5 :
            route.add((x, y, d))
            y -= 1
            route.add((x, y, 'U'))
        elif d == 'R' and x < 5:
            route.add((x, y, d))
            x += 1
            route.add((x, y, 'L'))

    return len(route) // 2

dirs = "ULURRDLLU"
print(solution(dirs))

dirs = "LULLLLLLU"
print(solution(dirs))

dirs = 'LRLRL'
print(solution(dirs))


'''
U 0,0 0,1
L 0,1 -1,1
U -1,1 -1,2
R -1,2 0,2
R 0,2 1,2
D 1,2 1,1
L 1,1 0,1
L 0,1 -1,1
U -1,1 -1,2

'''