# 2021 카카오 채용연계형 인턴십 > 거리두기 확인하기
# https://programmers.co.kr/learn/courses/30/lessons/81302

def solution(places):
    answer = []

    places = [list(map(list, p)) for p in  places]

    area = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    for place in places :
        is_break = False
        is_keep = 1

        for y in range(5) :
            for x in range(5) :
                if place[y][x] == 'P' :
                    for move_x, move_y in area :
                        if y+move_y >= 0 and y+move_y < 5 and x+move_x >= 0 and x+move_x < 5 :
                            if place[y+move_y][x+move_x] == 'P' :
                                is_keep = 0
                                is_break = True

                        if is_break :
                            break
                elif place[y][x] == 'O' :
                    cnt = 0
                    for move_x, move_y in area :
                        if y+move_y >= 0 and y+move_y < 5 and x+move_x >= 0 and x+move_x < 5 :
                            if place[y+move_y][x+move_x] == 'P' :
                                cnt += 1
                                if cnt > 1 :
                                    is_keep = 0
                                    is_break = True
                        
                        if is_break :
                            break

                if is_break :
                    break
            if is_break :
                break     

        answer.append(is_keep)
        
    return answer

places = [["POOOP", 
           "OXXOX", 
           "OPXPX", 
           "OOXOX", 
           "POXXP"], 
          ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
          ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))