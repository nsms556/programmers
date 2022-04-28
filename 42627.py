# 힙(Heap) > 디스크 컨트롤러
# https://programmers.co.kr/learn/courses/30/lessons/42627

import heapq
from itertools import accumulate

def process_queue(queue, t, completed) :
    job, req = heapq.heappop(queue)
    t += job

    completed.append((req, t))

    return t

def solution(jobs):
    jobs.sort(reverse=True)

    queue = []
    completed = []

    t = 0
    while jobs or queue :
        while jobs and jobs[-1][0] <= t :
            heapq.heappush(queue, tuple(reversed(jobs.pop())))

        if queue :
            t = process_queue(queue, t, completed)
        elif jobs :
            t = jobs[-1][0]

    answer = [res - req for req, res in completed]
    answer = sum(answer) // len(answer)

    return answer

jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))

jobs = [[0, 3], [0, 9], [0, 6]]
print(solution(jobs))

jobs = [[0, 3], [3, 3], [6, 1]]
print(solution(jobs))

jobs = [[0, 3], [4, 3], [9, 1]]
print(solution(jobs))