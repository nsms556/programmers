# 그래프 > 순위
# https://programmers.co.kr/learn/courses/30/lessons/49191

def solution(n, results):
    answer = 0

    wins = {i:set() for i in range(1, n+1)}
    loses = {i:set() for i in range(1, n+1)}

    for win, lose in results :
        wins[win].add(lose)
        loses[lose].add(win)

    for k, values in wins.items() :
        for v in values :
            loses[v] = loses[v] | loses[k]

    for k, values in loses.items() :
        for v in values :
            wins[v] = wins[v] | wins[k]

    for k, values in list(wins.items())[::-1] :
        for v in values :
            loses[v] = loses[v] | loses[k]

    for k, values in list(loses.items())[::-1] :
        for v in values :
            wins[v] = wins[v] | wins[k]
    
    for i in wins :
        if len(wins[i]) + len(loses[i]) == n-1 :
            answer += 1

    return answer

n, results = 5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(n, results))