# 위클리 챌린지 > 전력망을 둘로 나누기
# https://programmers.co.kr/learn/courses/30/lessons/86971

from collections import defaultdict

def solution(n, wires) :    
    answer = 100

    tree = defaultdict(list)
    for p, c in wires :
        tree[p].append(c)
        tree[c].append(p)

    def dfs(head) :
        visited = []
        queue = [head]

        while len(queue) != 0 :
            now = queue.pop(0)
            queue.extend([node for node in tree[now] if node not in visited])

            visited.append(now)
    
        return len(visited)

    for p, c in wires :
        tree[p].remove(c)
        tree[c].remove(p)
        answer = min(answer, abs(n - dfs(p) * 2))
        tree[p].append(c)
        tree[c].append(p)

    return answer

n, wires = 9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
print(solution(n, wires))

n, wires = 4, [[1,2],[2,3],[3,4]]
print(solution(n, wires))

n, wires = 7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]
print(solution(n, wires))