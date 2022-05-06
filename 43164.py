# 깊이/너비 우선 탐색(DFS/BFS) > 여행경로
# https://programmers.co.kr/learn/courses/30/lessons/43164

from collections import defaultdict    

def solution(tickets):
    graph = defaultdict(list)

    for s, e in tickets :
        graph[s].append(e)

    for port in graph :
        graph[port].sort(reverse=True)

    stack = []
    stack.append('ICN')
    path = []

    while stack :
        port = stack[-1]

        if port not in graph or not graph[port] :
            path.append(stack.pop())
        else :
            stack.append(graph[port].pop())

    answer = path[::-1]
    
    return answer

tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
print(solution(tickets))

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(solution(tickets))
