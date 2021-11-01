# 1101 월간 코드 챌린지 시즌1 3진법 뒤집기
# https://programmers.co.kr/learn/courses/30/lessons/68935

def convert(num) :
    q, r = divmod(num, 3)
    if q == 0 :
        return str(r)
    else :
        return convert(q) + str(r)

def solution(n):
    answer = convert(n)

    answer = int(''.join(reversed(answer)), 3)

    return answer

n = 45
print(solution(n))

n = 125
print(solution(n))