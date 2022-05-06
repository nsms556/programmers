# 깊이/너비 우선 탐색(DFS/BFS) > 네트워크
# https://programmers.co.kr/learn/courses/30/lessons/43162

from collections import defaultdict, deque


def solution(n, computers):
    answer = 0

    l = len(computers)

    graph = defaultdict(set)
    for i, conns in enumerate(computers) :
        for j, conn in enumerate(conns) :
            if conn and i != j:
                graph[i].add(j)

    not_visited = list(range(l))
    queue = deque()
    queue.append(not_visited.pop())
    
    while queue:
        node = queue.popleft()

        for dest in graph[node] :
            if dest in not_visited and dest not in queue :
                queue.append(dest)
                not_visited.remove(dest)

        if not queue :
            answer += 1

            if not_visited :
                queue.append(not_visited.pop())
            
    return answer

n, computers = 3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n, computers))

n, computers = 3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n, computers))
