# 완전탐색 > 소수 찾기
# https://programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations

def is_prime(n) :
    if n < 2 :
        return False

    for i in range(2, int(n ** 0.5)+1) :
        if n % i == 0 :
            return False

    return True

def solution(numbers):
    answer = 0

    piece = list(numbers)

    n = []
    for i in range(1, len(piece)+1) :
        n.extend(list(permutations(piece, i)))

    n = set(map(int, map(''.join, n)))
    
    for i in n :
        if is_prime(i) :
            answer += 1

    return answer

numbers = '17'
print(solution(numbers))

numbers = '011'
print(solution(numbers))