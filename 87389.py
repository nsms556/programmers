# 1027 월간 코드 챌린지 시즌3 나머지가 1이 되는 수 찾기
# https://programmers.co.kr/learn/courses/30/lessons/87389

def solution(n):
    answer = [i for i in range(3,n+1) if n % i == 1]

    return min(answer)

n = 10
print(solution(n))

n = 12
print(solution(n))