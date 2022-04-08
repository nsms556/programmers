# 연습문제 > 하노이의 탑
# https://programmers.co.kr/learn/courses/30/lessons/12946

def solution(n):
    answer = []

    def hanoi(n, start, mid, end) :
        if n == 1 :
            answer.append([start, end])
            return
        else :
            hanoi(n-1, start, end, mid)
            hanoi(1, start, mid, end)
            hanoi(n-1, mid, start, end)

    hanoi(n, 1,2,3)

    return answer

n = 2
print(solution(n))