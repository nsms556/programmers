# 1103 탐욕법(Greedy) 체육복
# https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    uniform = [1] * (n+2)

    for i in lost :
        uniform[i] -= 1

    for i in reserve :
        uniform[i] += 1

    rsv = [x for x in reserve if x not in lost]

    for i in sorted(rsv) :
        if uniform[i-1] == 0 :
            uniform[i-1] = 1
            uniform[i] = 1
        elif uniform[i+1] == 0 :
            uniform[i+1] = 1
            uniform[i] = 1
    
    return n - uniform.count(0)

def solution(n, lost, reserve) :
    t_reserve = [x for x in reserve if x not in lost]
    t_lost = [x for x in lost if x not in reserve]

    for r in t_reserve :
        front = r - 1
        back = r + 1

        if front in t_lost :
            t_lost.remove(front)
        elif back in t_lost :
            t_lost.remove(back)

    return n - len(t_lost)

n, lost, reserve = 5, [2, 4], [1, 3, 5]
print(solution(n, lost, reserve))

n, lost, reserve = 5,[2, 4], [3]
print(solution(n, lost, reserve))

n, lost, reserve = 3, [3], [1]
print(solution(n, lost, reserve))