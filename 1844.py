# 찾아라 프로그래밍 마에스터 > 게임 맵 최단거리
# https://programmers.co.kr/learn/courses/30/lessons/1844

from collections import deque
    
def solution(maps):
    n = len(maps)
    m = len(maps[0])

    queue = deque()
    maps[0][0] = 0
    queue.append((0,0,1))

    while queue :
        x, y, distance = queue.popleft()
        
        if (x, y) == (m-1, n-1) :
            return distance

        if x-1 >= 0 and maps[y][x-1] :
            maps[y][x-1] = 0
            queue.append((x-1, y, distance+1))
        if y-1 >= 0 and maps[y-1][x] :
            maps[y-1][x] = 0
            queue.append((x, y-1, distance+1))
        if x+1 <= m-1 and maps[y][x+1] :
            maps[y][x+1] = 0
            queue.append((x+1, y, distance+1))
        if y+1 <= n-1 and maps[y+1][x] :
            maps[y+1][x] = 0
            queue.append((x, y+1, distance+1))

    return -1

maps = [[1,0,1,1,1],
        [1,0,1,0,1],
        [1,0,1,1,1],
        [1,1,1,0,1],
        [0,0,0,0,1]]
print(solution(maps))

maps = [[1,0,1,1,1],
        [1,0,1,0,1],
        [1,0,1,1,1],
        [1,1,1,0,0],
        [0,0,0,0,1]]
print(solution(maps))

maps = [[1,0,1,1,1],
        [1,0,1,0,1],
        [1,0,1,0,1],
        [1,0,1,0,1],
        [1,1,1,0,1]]
print(solution(maps))

maps = [[1,1,1,1,1],
        [0,0,1,0,1],
        [1,0,1,0,1],
        [1,0,1,0,1],
        [1,1,1,0,1]]
print(solution(maps))

maps = [[1,1,1,1,0],
        [0,0,1,0,1],
        [1,0,1,0,1],
        [1,0,1,1,1],
        [1,1,1,0,1]]
print(solution(maps))

maps = [[1,1],
        [1,1]]
print(solution(maps))

maps = [[1,1,1],
        [1,1,1],
        [1,1,1]]
print(solution(maps))