# 탐욕법(Greedy) > 큰 수 만들기
# https://programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    queue = []

    for idx, num in enumerate(number) :
        while queue and queue[-1] < num and k > 0 :
            queue.pop()
            k -= 1

        if k == 0 :
            queue.extend(number[idx:])
            break

        queue.append(num)

    if k > 0 :
        queue = queue[:-k]

    return ''.join(queue)

number, k = '1924', 2
print(solution(number, k))

number, k = '1231234', 3
print(solution(number, k))

number, k = '4177252841', 4
print(solution(number, k))