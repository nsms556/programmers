# 1020 소수 찾기
# https://programmers.co.kr/learn/courses/30/lessons/12921

def is_prime(num) :
    for i in range(2, int(num ** (1/2))+1) :
        if num % i == 0 :
            return False

    return True

def solution(n):
    cnt = 0

    for i in range(2, n+1) :
        if is_prime(i) :
            cnt += 1

    return cnt

def solution(n) :
    nums = set(range(2, n+1))

    for i in range(2, n+1) :
        if i in nums :
            nums -= set(range(2*i, n+1, i))

    return len(nums)
    
n = 10
print(solution(n))

n = 5
print(solution(n))
