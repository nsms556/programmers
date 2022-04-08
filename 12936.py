# 연습문제 > 줄 서는 방법
# https://programmers.co.kr/learn/courses/30/lessons/12936

from math import factorial

def solution(n, k):
    answer = []

    people = list(range(1, n+1))

    while n :
        person_cycle = factorial(n-1)
        number, next_k = divmod(k, person_cycle)
        number = int(number)

        if next_k == 0 :
            next_k = person_cycle
            number -= 1

        answer.append(people.pop(number))

        k = next_k
        n -= 1

    return answer

n, k = 3, 5
print(solution(n, k))

n, k = 4, 24
print(solution(n, k))

n, k = 20, 1
print(solution(n, k))