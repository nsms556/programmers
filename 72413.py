# 2021 KAKAO BLIND RECRUITMENT > 합승 택시 요금
# https://programmers.co.kr/learn/courses/30/lessons/72413

from collections import defaultdict
import heapq

def djikstra(graph, start) :
    distances = {node:float('inf') for node in graph}
    distances[start] = 0

    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue :
        curr_dist, curr_dest = heapq.heappop(queue)

        if distances[curr_dest] < curr_dist :
            continue

        for new_dest, new_dist in graph[curr_dest].items() :
            dist = curr_dist + new_dist

            if dist < distances[new_dest] :
                distances[new_dest] = dist
                heapq.heappush(queue, [dist, new_dest])

    return distances

def solution(n, s, a, b, fares):
    costs = defaultdict(dict)

    for start, end, cost in fares :
        costs[start][end] = cost
        costs[end][start] = cost

    a_cost = djikstra(costs, a)
    b_cost = djikstra(costs, b)
    s_cost = djikstra(costs, s)

    cost_sum = {}
    for i in a_cost :
        cost_sum[i] = a_cost[i] + b_cost[i] + s_cost[i]

    answer = min(cost_sum.values())

    return answer

n, s, a, b, fares = 6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
print(solution(n,s, a, b, fares))

n, s, a, b, fares = 7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]
print(solution(n,s, a, b, fares))

n, s, a, b, fares = 6, 4, 5, 6, [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]
print(solution(n,s, a, b, fares))
