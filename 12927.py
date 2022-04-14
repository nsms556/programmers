# 연습문제 > 야근 지수
# https://programmers.co.kr/learn/courses/30/lessons/12927

import heapq

def solution(n, works):
    if sum(works) < n :
        return 0

    heap = []
    for i in works :
        heapq.heappush(heap, -i)

    while n :
        heapq.heappush(heap, heapq.heappop(heap) + 1)
        n -= 1

    return sum([i * i for i in heap])

works, n = [4, 3, 3], 4
print(solution(n, works))

works, n = [2, 1, 2], 1
print(solution(n, works))

works, n = [1,1], 3
print(solution(n, works))
