# 1117 연습문제 > 숫자의 표현
# https://programmers.co.kr/learn/courses/30/lessons/12924

def solution(n):
    answer = 0
    
    d = {}
    s = i = 0
    while s < n :
        i += 1
        s += i
        d[i] = [s]
    
    for key in d :
        s = d[key][0]
        while s < n :
            s += key
            d[key].append(s)

    for v in d.values() :
        if n in v :
            answer += 1

    return answer

n = 15
print(solution(n))

n = 44
print(solution(n))

'''
3 1+2 -> 1
5 2+3 -> 1
6 1+2+3 -> 1
7 3+4 -> 1
9 2+3+4 5+4 -> 2
10 1+2+3+4 -> 1
11 5+6 -> 1
12 3+4+5 -> 1
13 6+7 -> 1
14 2+3+4+5 -> 1

'''
