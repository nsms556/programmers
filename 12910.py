# 1021 나누어 떨어지는 숫자 배열
# https://programmers.co.kr/learn/courses/30/lessons/12910

def solution(arr, divisor):
    answer = [num for num in arr if num % divisor == 0]

    if len(answer) == 0 :
        answer = [-1]
    else :
        answer = sorted(answer)

    return answer

arr, divisor = [5, 9, 7, 10], 5
print(solution(arr, divisor))

arr, divisor = [2, 36, 1, 3], 1
print(solution(arr, divisor))

arr, divisor = [3, 2, 6], 10
print(solution(arr, divisor))