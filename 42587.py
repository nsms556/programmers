# 스택/큐 > 프린터
# https://programmers.co.kr/learn/courses/30/lessons/42587
 
from collections import deque

def solution(priorities, location):
    answer = 0

    queue = deque(enumerate(priorities))
    
    while queue :
        if queue[0][1] < max(queue, key=lambda x : x[1])[1] :
            queue.rotate(1)
        else :
            printed = queue.popleft()
            answer += 1
            if printed[0] == location :
                break

    return answer

def solution(priorities, location):
    answer = 0

    queue = deque(enumerate(priorities))
    
    while queue :
        item = queue.popleft()
        if not queue :
            answer += 1
            break
        else :
            if item[1] < max(queue, key=lambda x : x[1])[1] :
                queue.append(item)
            else :
                answer += 1
                if item[0] == location :
                    break

    return answer

priorities, location = [2, 1, 3, 2], 2
print(solution(priorities, location))

priorities, location = [1, 1, 9, 1, 1, 1], 0
print(solution(priorities, location))

priorities, location = [1, 1, 1, 1, 1, 1], 3
print(solution(priorities, location))

priorities, location = [2, 3, 3, 2, 9, 3, 3], 3
print(solution(priorities, location))

priorities, location = [3,3,4,2], 3
print(solution(priorities, location))

priorities, location = [2], 0
print(solution(priorities, location))

priorities, location = [2, 4, 8, 2, 9, 3, 3], 2
print(solution(priorities, location))

priorities, location = [2, 4, 8, 2, 9, 3, 3], 4
print(solution(priorities, location))

priorities, location = [1,2,8,3,4], 4
print(solution(priorities, location))

