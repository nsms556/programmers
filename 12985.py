# 2017 팁스타운 > 예상 대진표
# https://programmers.co.kr/learn/courses/30/lessons/12985

from math import ceil, log2

def solution(n,a,b):
    answer = int(log2(n))

    a, b = (a, b) if a < b else (b, a)

    while not (a <= 2**(answer-1) and b > 2**(answer-1)) :
        answer -= 1

    return answer

def solution(n,a,b):
    answer = 0

    while a != b :
        answer += 1
        a = ceil(a / 2)
        b = ceil(b / 2)

    return answer

def solution(n,a,b):
    return ((a-1) ^ (b-1)).bit_length()

N, A, B = 8, 4, 7
print(solution(N, A, B))

N, A, B = 128, 1, 9
print(solution(N, A, B))

N, A, B = 256, 2, 255
print(solution(N, A, B))
'''
128 1 9 0 3
1 9  1
1 5  2
1 3  3
1 2  4
1 1  0

0   0000
8   1000
xor 1000 -> 4

256 2 255 1 7.x
2 255   1
1 128   2
1 64    3
1 32    4
1 16    5
1 8     6
1 4     7
1 2     8
1 1     9

1   00000001
254 11111110
xor 11111111

32 18 31 4.x 4.x
9 16    1
5 8     2
3 4     3
2 2     4

17  10001
30  11110
xor 01111

'''