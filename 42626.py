# 힙(Heap) > 더 맵게
# https://programmers.co.kr/learn/courses/30/lessons/42626

import heapq

def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)

    while scoville[0] < K :
        if len(scoville) > 1 :
            heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville) * 2)
            answer += 1
        else :
            answer = -1
            break

    return answer

scoville, K = [1, 2, 3, 9, 10, 12], 7
print(solution(scoville, K))