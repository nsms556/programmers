# 정렬 > 가장 큰 수
# https://programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    numbers = sorted(list(map(str, numbers)), reverse=True, key=lambda x : x*3)

    return ''.join(numbers)

numbers = [6, 10, 2]
print(solution(numbers))

numbers = [3, 30, 34, 5, 9]
print(solution(numbers))

numbers = [1, 10, 20, 2]
print(solution(numbers))

numbers = [0, 0, 0]
print(solution(numbers))