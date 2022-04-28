# 탐욕법(Greedy) > 섬 연결하기
# https://programmers.co.kr/learn/courses/30/lessons/42861
# 최소 신장 트리
# https://hillier.tistory.com/54

import heapq

def prim(graph) :
    total_cost = 0

    visited = []
    queue = []

    start = 0
    start_cost = graph[start][start]
    cnt = 0

    heapq.heappush(queue, (start, start_cost))

    while queue :
        if cnt == n :
            break

        curr_node, curr_cost = heapq.heappop(queue)

        if curr_node not in visited :
            visited.append(curr_node)
            total_cost += curr_cost
            cnt += 1

            for new_node in graph[curr_node].items() :
                heapq.heappush(queue, new_node)

    return total_cost

def kruskal(n, lines) :
    total_cost = 0

    roots = [i for i in range(n)]

    def find(x) :
        if x != roots[x] :
            roots[x] = find(roots[x])

        return roots[x]

    lines.sort(key=lambda x : x[2])

    for s, e, c in lines :
        s_node = find(s)
        e_node = find(e)

        if s_node != e_node :
            if s_node > e_node :
                roots[s_node] = e_node
            else :
                roots[e_node] = s_node
            total_cost += c

    return total_cost

def solution(n, costs):
    answer = 0

    min_cost = {i:{} for i in range(n)}

    for s, e, c in costs :
        min_cost[s][e] = c
        min_cost[e][s] = c
    
    for i in range(n) :
        min_cost[i][i] = 0

    for k in min_cost :
        print(min_cost[k])

    answer = prim(min_cost)

    return answer

def solution(n, costs):
    total_cost = 0

    roots = [i for i in range(n)]

    def find(x) :
        if x != roots[x] :
            roots[x] = find(roots[x])

        return roots[x]

    costs.sort(key=lambda x : x[2])

    for s, e, c in costs :
        s_node = find(s)
        e_node = find(e)

        if s_node != e_node :
            if s_node > e_node :
                roots[s_node] = e_node
            else :
                roots[e_node] = s_node
            total_cost += c

    return total_cost

n, costs = 4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
print(solution(n, costs))

n, costs = 4, [[0,1,1],[0,2,1],[0,3,1],[1,3,200],[2,3,5000]]
print(solution(n, costs))
