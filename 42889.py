# 1103 2019 KAKAKO BLIND RECRUITMENT 실패율
# https://programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    stopped = {i:0 for i in range(N+1)}
    for i in set(stages) :
        stopped[i] = stages.count(i)

    cleared = {}
    cleared[0] = len(stages)
    for i in range(1,N+1) :
        cleared[i] = cleared[i-1] - stopped[i]

    fail = {}
    for i in range(1,N+1) :
        if cleared[i-1] == 0 :
            fail[i] = 0
        else :
            fail[i] = 1 - cleared[i] / cleared[i-1]

    answer = sorted(fail.keys(), key=lambda x : fail[x], reverse=True)
    return answer

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))

N = 4
stages = [4,4,4,4,4]
print(solution(N, stages))

N = 5
stages = [1,2,3,4,3]
print(solution(N, stages))