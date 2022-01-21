# Summer/Winter Coding(~2018) > 배달
# https://programmers.co.kr/learn/courses/30/lessons/12978

from collections import defaultdict
import heapq

def solution(N, road, K):
    answer = 0

    graph = defaultdict(dict)

    for r in road :
        s, e, c = r
        if e in graph[s] :
            graph[s][e] = min(graph[s][e], c)
            graph[e][s] = min(graph[s][e], c)
        else :
            graph[s][e] = c
            graph[e][s] = c

    for i in range(1, N+1) :
        graph[i][i] = 0
    
    distances = {i : 500000 for i in graph}
    distances[1] = 0

    queue = []
    heapq.heappush(queue, (0, 1))

    while queue :
        c, dest = heapq.heappop(queue)

        if distances[dest] < c :
            continue

        for new_dest, new_cost in graph[dest].items() :
            cost = c + new_cost
            if cost < distances[new_dest] :
                distances[new_dest] = cost
                heapq.heappush(queue, (cost, new_dest))

    answer = len([i for i in distances.values() if i <= K])

    return answer

N, road, K = 5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3
print(solution(N, road, K))

N, road, K = 6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4
print(solution(N, road, K))
