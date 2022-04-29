# 월간 코드 챌린지 시즌1 > 스타 수열
# https://programmers.co.kr/learn/courses/30/lessons/70130
# https://yabmoons.tistory.com/610

from collections import Counter

def solution(a):
    answer = 0

    c = Counter(a)

    for most in c :
        if c[most] <= answer :
            continue

        ret = 0
        i = 0
        while i < len(a)-1 :
            if a[i] != most and a[i+1] != most :
                i += 1
                continue
            elif a[i] == a[i+1] :
                i += 1
                continue
            else :
                ret += 1
                i += 1
            
            i += 1

        answer = max(answer, ret)

    return answer * 2

a = [1,2,1,3,1,4,1,5,3,1]
print(solution(a))

a = [0]
print(solution(a))

a = [5,2,3,3,5,3]
print(solution(a))

a = [0,3,3,0,7,2,0,2,2,0]
print(solution(a))
