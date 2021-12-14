# 월간 코드 챌린지 시즌1 > 이진 변환 반복하기
# https://programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    answer = [0, 0]

    while s != '1' :
        answer[1] += s.count('0')
        s = bin(s.count('1'))[2:]
        answer[0] += 1

    return answer

s = '110010101001'
print(solution(s))

s = '01110'
print(solution(s))

s = '1111111'
print(solution(s))