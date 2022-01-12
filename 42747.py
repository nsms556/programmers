# 정렬 > H-Index
# https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    answer = 0
    citations.sort()

    for h in citations :
        cnt = 0
        for c in citations :
            if c >= h :
                cnt += 1

        if h > answer and cnt > answer :
            answer = min(h, cnt)

    return answer

citations = [3, 0, 6, 1, 5]
print(solution(citations))

citations = [4,3,2,1,1,8,9]
print(solution(citations))

citations = [5, 8]
print(solution(citations))

citations = [3,0,3,6,1,5]
print(solution(citations))

citations = [0,0,0]
print(solution(citations))

citations = [0,1,1]
print(solution(citations))

citations = [0,1,2]
print(solution(citations))

'''
6 5 3 3 1 0
1 2 3 4 5 6

9 8 4 3 2 1 1
1 2 3 4 5 6 7
'''