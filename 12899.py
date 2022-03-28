# 연습문제 > 124 나라의 숫자
# https://programmers.co.kr/learn/courses/30/lessons/12899

def convert(n, base) :
    ret = []

    while n :
        m = n % 3
        if not m :
            m = 3
            n -= 1
        
        ret.append(str(m))

        n //= 3

    return ret

def solution(n):
    answer = convert(n, 3)

    for i in range(len(answer)) :
        if answer[i] == '3' :
            answer[i] = '4'

    return ''.join(reversed(answer))

n = 1
print(solution(n))

n = 2
print(solution(n))

n = 3
print(solution(n))

n = 4
print(solution(n))

n = 9
print(solution(n))

n = 14
print(solution(n))

n = 20
print(solution(n))

'''
1 1     a   1   1
2 2     b   2   2
3 4     c   3   10
4 11    aa  11  11    
5 12    ab  12  12
6 14    ac  13  20
7 21    ba  21  21
8 22    bb  22  22
9 24    bc  23  100
10 41   ca  31  101
11 42       32  102
12 44       33  110
13 111      111 111
14 112      112 112
15 114      113 120
16 121      121 121
17 122      122 122
18 124      123 200
'''