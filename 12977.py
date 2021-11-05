# 1105 Summer/Winter Coding(~2018) 소수 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12977

from itertools import combinations

def is_prime(num) :
    for i in range(2, int(num**(1/2)+1)) :
        if num % i == 0 :
            return False
    
    return True

def solution(nums):
    cnt = 0
    for i in combinations(nums, 3) :
        if is_prime(sum(i)) :
            cnt += 1
    
    return cnt
    
nums = [1,2,3,4]
print(solution(nums))

nums = [1,2,7,6,4]
print(solution(nums))