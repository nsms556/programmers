# 1103 찾아라 프로그래밍 마에스터 폰켓몬
# https://programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    return min(len(nums)//2, len(set(nums)))

nums = [3,1,2,3]
print(solution(nums))

nums = [3,3,3,2,2,4]
print(solution(nums))

nums = [3,3,3,2,2,2]
print(solution(nums))

nums = [1,1,1,1,2,2,3,3,4,4,2,1,24,12,42,4,2,5]
print(solution(nums))