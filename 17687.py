# 2018 KAKAO BLIND RECRUITMENT > [3차] n진수 게임
# https://programmers.co.kr/learn/courses/30/lessons/17687

def convert(num, base) :
    c = '0123456789ABCDEF'
    q, r = divmod(num, base)
    if q == 0 :
        return c[r]
    else :
        return convert(q, base) + c[r]

def solution(n, t, m, p):
    answer = ''

    tmp = 0
    while len(answer) < t * m :
        answer += convert(tmp, n)
        tmp += 1

    answer = answer[p-1::m][:t]
    return answer

n, t, m, p = 2,4,2,1
print(solution(n,t,m,p))

n, t, m, p = 16, 16, 2, 1
print(solution(n,t,m,p))

n, t, m, p = 16, 16, 2, 2
print(solution(n,t,m,p))

'''
0 1 10 11 100 101 110 111 1000
0 1 2 3 4 5 6 7 8 9 A B C D E F 10 11 12 13 14 15 16 17 18
'''