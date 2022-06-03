# 연습문제 > 숫자 블록
# https://programmers.co.kr/learn/courses/30/lessons/12923

def solution(begin, end):
    answer = []

    for i in range(begin, end+1) :
        if i == 1 :
            answer.append(0)
            continue

        block = 1    
        for b in range(2, int(i ** 0.5)+1) :
            if i % b == 0 :
                if i // b > 10000000 :
                    continue
                else :
                    block = i // b
                    break

        answer.append(block)

    return answer

begin, end = 1, 10
print(solution(begin, end))

begin, end = 121, 150
print(solution(begin, end))

begin, end = 999999991, 1000000000
print(solution(begin, end))
