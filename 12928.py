# 1018 약수의 합
# https://programmers.co.kr/learn/courses/30/lessons/12928

def solution(n):
    l = set()

    for i in range(1, int(n**(1/2))+1) :
        if n % i == 0 :
            l.add(i)
            l.add(n // i)

    return sum(l)

n = 12
print(solution(n))

n = 5
print(solution(n))

n = 1
print(solution(n))

n = 2
print(solution(n))
