# 1115 연습문제 > N개의 최소공배수
# https://programmers.co.kr/learn/courses/30/lessons/12953

def gcd(a, b) :
    if a % b == 0 :
        return b
    else :
        return gcd(b, a%b)

def lcm(a, b) :
    return int(a * b / gcd(a, b))

def solution(arr):
    a = 1
    
    for b in arr :
        a = lcm(a, b)

    return a

arr = [2,6,8,14]
print(solution(arr))

arr = [1,2,3]
print(solution(arr))

arr = [2,3,5,8]
print(solution(arr))