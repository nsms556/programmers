# 월간 코드 챌린지 시즌2 > 모두 0으로 만들기
# https://programmers.co.kr/learn/courses/30/lessons/76503

import sys
sys.setrecursionlimit(600000)

def solution(a, edges):
    answer = 0

    if sum(a) != 0 :
        return -1

    graph = {i : [] for i in range(len(a))}

    for s, e in edges :
        graph[s].append(e)
        graph[e].append(s)

    visited = [0 for _ in range(len(a))]

    def dfs(node) :
        nonlocal answer

        w = a[node]
        visited[node] = 1

        juniors = [j for j in graph[node] if visited[j] == 0]

        for j in juniors :
            w += dfs(j)

        answer += abs(w)

        return w

    dfs(0)

    return answer

a, edges = [-5,0,2,1,2], [[0,1],[3,4],[2,3],[0,3]]
print(solution(a, edges))

a, edges = [0,1,0], [[0,1],[1,2]]
print(solution(a, edges))
