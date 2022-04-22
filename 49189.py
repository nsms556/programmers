# 그래프 > 가장 먼 노드
# https://programmers.co.kr/learn/courses/30/lessons/49189

from collections import defaultdict, deque

def solution(n, edge):
    answer = {}
    graph = defaultdict(list)

    dis = {i:-1 for i in range(1, n+1)}
    dis[1] = 0

    for s, e in edge :
        graph[s].append(e)
        graph[e].append(s)

    q = deque([1])
    d_max = -1

    while q :
        node = q.popleft()

        for new_node in graph[node] :
            if dis[new_node] == -1 :
                q.append(new_node)
                dis[new_node] = dis[node] + 1
                answer[dis[new_node]] = answer.get(dis[new_node], 0) + 1

                d_max = max(d_max, dis[new_node])
    
    return answer[d_max]

n, vertex = 6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, vertex))