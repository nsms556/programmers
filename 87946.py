# 위클리 챌린지 > 피로도
# https://programmers.co.kr/learn/courses/30/lessons/87946

from itertools import permutations

def solution(k, dungeons):
    answers = []
    enter = permutations(dungeons, len(dungeons))
    
    for e in enter :
        tired = k
        answer = 0
        print(e)
        for d in e :
            if d[0] <= tired :
                tired -= d[1]
                answer += 1
            else :
                continue
        
        answers.append(answer)

    return max(answers)

def solution(k, dungeons):
    answer = 0
    l = len(dungeons)
    visited = [0] * l
    
    def dfs(k, cnt, dungeons) :
        print(k, cnt, visited)
        nonlocal answer
        if cnt > answer :
            answer = cnt

        for j in range(l) :
            if k >= dungeons[j][0] and not visited[j] :
                visited[j] = 1
                dfs(k-dungeons[j][1], cnt+1, dungeons)
                visited[j] = 0

    dfs(k, 0, dungeons)

    return answer
'''
[0 0 0], 80
[[80, 20], [50, 40], [30, 10]]


'''



k, dungeons = 80, [[80,20],[50,40],[30,10]]
print(solution(k, dungeons))

k, dungeons = 10, [[8,3],[8,2],[5,4]]
print(solution(k, dungeons))