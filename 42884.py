# 탐욕법(Greedy) > 단속카메라
# https://programmers.co.kr/learn/courses/30/lessons/42884

def solution(routes):
    answer = 0

    routes = sorted(routes, key=lambda x : x[1])

    camera = -30001

    for s, e in routes :
        if s > camera :
            answer += 1
            camera = e

    return answer

routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
print(solution(routes))
