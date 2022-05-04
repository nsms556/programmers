# 월간 코드 챌린지 시즌3 > 공 이동 시뮬레이션
# https://programmers.co.kr/learn/courses/30/lessons/87391
# https://programmers.co.kr/questions/29706

def solution(n, m, x, y, queries):
    answer = 0

    p1 = [x, y]
    p2 = [x, y]

    for d, dis in queries[::-1] :
        if d == 0 :
            p1[1] = p1[1] + dis if p1[1] != 0 else p1[1]
            p2[1] = min(p2[1]+dis, m-1)
        elif d == 1 :
            p1[1] = max(p1[1]-dis, 0)
            p2[1] = p2[1] - dis if p2[1] != m-1 else p2[1]
        elif d == 2 :
            p1[0] = p1[0] + dis if p1[0] != 0 else p1[0]
            p2[0] = min(p2[0]+dis, n-1)
        elif d == 3 :
            p1[0] = max(p1[0]-dis, 0)
            p2[0] = p2[0] - dis if p2[0] != n-1 else p2[0]
            
        if p1[0] >= n or p2[0] < 0 or p1[1] >= m or p2[1] < 0 :
            answer = -1
            break

    answer = (p2[0] - p1[0] + 1) * (p2[1] - p1[1] + 1) if answer != -1 else 0

    return answer

n, m, x, y, queries = 2, 2, 0, 0, [[2,1],[0,1],[1,1],[0,1],[2,1]]
print(solution(n, m, x, y, queries))

n, m, x, y, queries = 2, 5, 0, 1, [[3,1],[2,2],[1,1],[2,3],[0,1],[2,1]]
print(solution(n, m, x, y, queries))

n, m, x, y, queries = 1000, 1000, 1, 1, [[0,100001],[2,100001]]
print(solution(n, m, x, y, queries)) 