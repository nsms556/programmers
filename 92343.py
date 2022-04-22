# 2022 KAKAO BLIND RECRUITMENT > 양과 늑대
# https://programmers.co.kr/learn/courses/30/lessons/92343
# https://programmers.co.kr/questions/25736

def solution(info, edges):
    answer = 0

    graph = {i:[] for i in range(len(info))}

    for k, v in edges :
        graph[k].append(v)

    def dfs(node, sheep, wolf, visitable) :
        #print(node, sheep, wolf, visitable)

        nonlocal answer, graph

        if info[node] :
            wolf += 1
        else :
            sheep += 1

        answer = max(answer, sheep)

        if wolf >= sheep :
            return

        for i in range(len(visitable)) :
            new_visit = visitable[:i] + visitable[i+1:] + graph[visitable[i]]
            dfs(visitable[i], sheep, wolf, new_visit)

    start = 0
    dfs(start, 0, 0, graph[start])
    
    return answer

info, edges = [0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
print(solution(info, edges))

info, edges = [0,1,0,1,1,0,1,0,0,1,0], [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]
print(solution(info, edges))
