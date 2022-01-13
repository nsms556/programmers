# 스택/큐 > 다리를 지나는 트럭
# https://programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0

    truck_weights.reverse()
    bridge = deque([0] * bridge_length)
    now_weights = 0

    while truck_weights :
        if bridge[0] != 0 :
            now_weights -= bridge[0]
            bridge[0] = 0
            
        bridge.rotate(-1)

        if now_weights + truck_weights[-1] <= weight :
            now_weights += truck_weights[-1]
            bridge[-1] = (truck_weights.pop())
            
        answer += 1

    answer += bridge_length
    
    return answer

bridge_length, weight, truck_weights = 2, 10, [7,4,5,6]
print(solution(bridge_length, weight, truck_weights))

bridge_length, weight, truck_weights = 100, 100, [10]
print(solution(bridge_length, weight, truck_weights))

bridge_length, weight, truck_weights = 100, 100, [10,10,10,10,10,10,10,10,10,10]
print(solution(bridge_length, weight, truck_weights))
