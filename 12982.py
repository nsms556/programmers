# 1101 Summer/Winter Coding(~2018) 예산
# https://programmers.co.kr/learn/courses/30/lessons/12982

def solution(d, budget):
    answer = 0

    price = 0
    for i in sorted(d) :
        if price + i <= budget :
            price += i
            answer += 1
        else :
            break

    return answer

d = [1,3,2,5,4]
budget = 9
print(solution(d,budget))

d = [2,2,3,3]
budget = 10
print(solution(d,budget))