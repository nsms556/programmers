# 1014 최대공약수와 최소공배수
# https://programmers.co.kr/learn/courses/30/lessons/12940

def gcd(i, j) :
    if i % j == 0 :
        return j
    else :
        return gcd(j, i % j)

def lcm(i, j, g) :
    return int(i * j / g)

def solution(n, m):
    if n < m :
        g = gcd(m, n)
    else :
        g = gcd(n, m)

    return [g, lcm(n, m, g)]

n, m = 3, 12
print(solution(n, m))

n, m = 2, 5
print(solution(n, m))