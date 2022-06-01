# 위클리 챌린지 > 아이템 줍기
# https://programmers.co.kr/learn/courses/30/lessons/87694
# https://programmers.co.kr/questions/21284

def print_2d(arr) :
    for r in arr :
        print(*r)

def draw_left(arr, fix_y, x1, x2) :
    for x in range(x1+1, x2+1) :
        if arr[fix_y][x] != 3 :
            arr[fix_y][x] = 2

def draw_right(arr, fix_y, x1, x2) :
    for x in range(x1, x2) :
        if arr[fix_y][x] != 1 :
            arr[fix_y][x] = 4

def draw_up(arr, fix_x, y1, y2) :
    for y in range(y1, y2) :
        if arr[y][fix_x] != 2 :
            arr[y][fix_x] = 1

def draw_down(arr, fix_x, y1, y2) :
    for y in range(y1+1, y2+1) :
        if arr[y][fix_x] != 4 :
            arr[y][fix_x] = 3
    
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0

    direction = {1:(1,0),2:(0, -1),3:(-1, 0),4:(0, 1)}

    h = max(max([y for _, _, _, y in rectangle]), characterY, itemY) + 2
    w = max(max([x for _, _, x, _ in rectangle]), characterX, itemX) + 2

    maps = [[0 for _ in range(w)] for _ in range(h)]

    for rect in rectangle :
        x1, y1, x2, y2 = rect

        draw_up(maps, x1, y1, y2)       # 1
        draw_right(maps, y2, x1, x2)    # 4
        draw_down(maps, x2, y1, y2)     # 3
        draw_left(maps, y1, x1, x2)     # 2

    cha = (characterY, characterX)
    item = (itemY, itemX)

    p = tuple(map(sum, zip(direction[maps[characterY][characterX]], [characterY, characterX])))

    full_path = 1
    while p != cha :
        if p == item :
            item_path = full_path

        y, x = p
        d = direction[maps[y][x]]

        p = (y + d[0], x + d[1])
        full_path += 1

    answer = min(item_path, full_path-item_path)

    return answer

rectangle, characterX, characterY, itemX, itemY = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8
print(solution(rectangle, characterX, characterY, itemX, itemY))

rectangle, characterX, characterY, itemX, itemY = [[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]], 9, 7, 6, 1
print(solution(rectangle, characterX, characterY, itemX, itemY))

rectangle, characterX, characterY, itemX, itemY = [[1,1,5,7]], 1, 1, 4, 7
print(solution(rectangle, characterX, characterY, itemX, itemY))

rectangle, characterX, characterY, itemX, itemY = [[2,1,7,5],[6,4,10,10]], 3, 1, 7, 10
print(solution(rectangle, characterX, characterY, itemX, itemY))

rectangle, characterX, characterY, itemX, itemY = [[2,2,5,5],[1,3,6,4],[3,1,4,6]], 1, 4, 6, 3
print(solution(rectangle, characterX, characterY, itemX, itemY))

