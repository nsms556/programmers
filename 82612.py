# 1027 위클리 챌린지 1주차 부족한 금액 계산하기
# https://programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):
    total = sum([price * i for i in range(1, count+1)])
    
    answer = total - money if total > money else 0
    return answer

def solution(price, money, count):
    total = count * (2 * price + (count-1) * price) // 2
    
    answer = total - money if total > money else 0
    return answer
    
price = 3
money = 20
count = 4
print(solution(price, money, count))