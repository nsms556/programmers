# 1020 서울에서 김서방 찾기
# https://programmers.co.kr/learn/courses/30/lessons/12919

def solution(seoul):
    answer = '김서방은 {}에 있다'

    return answer.format(seoul.index('Kim'))

seoul = ['Jane', 'Kim']
print(solution(seoul))