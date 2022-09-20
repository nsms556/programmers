# 2022 KAKAO TECH INTERNSHIP > 두 큐 합 같게 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/118667

from collections import deque

def solution(queue1, queue2):
    answer = 0

    s1 = sum(queue1)
    s2 = sum(queue2)
    max_try = (len(queue1) + len(queue2)) * 2 + 2

    queue1, queue2 = deque(queue1), deque(queue2)
    
    while s1 != s2 :
        if s1 > s2 :
            item = queue1.popleft()
            s1 -= item
            
            queue2.append(item)
            s2 += item
        elif s1 < s2 :
            item = queue2.popleft()
            s2 -= item
            
            queue1.append(item)
            s1 += item

        answer += 1

        if answer > max_try :
            answer = -1
            break

    return answer

queue1, queue2 = [3, 2, 7, 2], [4, 6, 5, 1]
print(solution(queue1, queue2))

queue1, queue2 = [1, 2, 1, 2], [1, 10, 1, 2]
print(solution(queue1, queue2))

queue1, queue2 = [1, 1], [1, 5]
print(solution(queue1, queue2))

queue1, queue2 = [1,1,1,8,10,9], [1,1,1,1,1,1]
print(solution(queue1, queue2))

queue1, queue2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 10], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print(solution(queue1, queue2))

queue1, queue2 = [1, 1, 1, 1, 1], [1, 1, 1, 9, 1]
print(solution(queue1, queue2))

'''
3 2 7 2     4 6 5 1
3 2 7 2 4   6 5 1
2 7 2 4     6 5 1 3
7 2 4       6 5 1 3 2
7 2 4 6     5 1 3 2
2 4 6       5 1 3 2 7
2 4 6 5     1 3 2 7
4 6 5       1 3 2 7 2
6 5         1 3 2 7 2 4
6 5 1       3 2 7 2 4
6 5 1 3     2 7 2 4
5 1 3       2 7 2 4 6
5 1 3 2     7 2 4 6
5 1 3 2 7   2 4 6
1 3 2 7     2 4 6 5
1 3 2 7 2   4 6 5
3 2 7 2     4 6 5 1
'''