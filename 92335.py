# 2022 KAKAO BLIND RECRUITMENT > k진수에서 소수 개수 구하기
# https://programmers.co.kr/learn/courses/30/lessons/92335

def convert(i, k) :
    ret = []

    while i :
        ret.append(str(i % k))
        i //= k

    return ''.join(reversed(ret))

def is_prime(p) :
    if p == 1 :
        return False
        
    for i in range(2, int(p ** 0.5) + 1) :
        if not p % i :
            return False

    return True

def solution(n, k):
    answer = 0

    prime = set()

    for p in convert(n, k).split('0') :
        if p :
            p = int(p)
        else :
            continue

        if p in prime :
            answer += 1
        elif is_prime(p) :
            answer += 1
            prime.add(p)
    
    return answer

n, k = 437674, 3
print(solution(n, k))

n, k = 110011, 10
print(solution(n, k))