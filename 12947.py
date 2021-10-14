# 1013 하샤드 수
# https://programmers.co.kr/learn/courses/30/lessons/12947
'''
def solution(x):
    origin_x = x

    s = 0
    while x > 0 :
        s += x % 10
        x //= 10

    answer = origin_x % s == 0

    return answer
'''
def solution(x) :
    s = sum([int(i) for i in str(x)])

    return x % s == 0

arr = 10
print(solution(arr))

arr = 12
print(solution(arr))

arr = 11
print(solution(arr))

arr = 13
print(solution(arr))