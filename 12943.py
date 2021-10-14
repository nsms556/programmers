# 1014 콜라츠 추측
# https://programmers.co.kr/learn/courses/30/lessons/12943

dic = {}

def collatz(i) :
    if i % 2 == 1 :
        return i * 3 + 1
    else :
        return i // 2

def solution(num):
    for answer in range(500) :
        if num == 1 :
            break
        else :
            num = collatz(num)

    if num != 1 :
        answer = -1
        
    return answer

n = 6
print(solution(n))

n = 16
print(solution(n))

n = 626331
print(solution(n))