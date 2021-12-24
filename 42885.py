# 탐욕법(Greedy) > 구명보트
# https://programmers.co.kr/learn/courses/30/lessons/42885

def solution(people, limit):
    answer = 0
    people.sort()

    left = 0
    right = len(people) - 1

    while left < right :
        if people[right] <= limit / 2 :
            break
        
        if people[left] + people[right] > limit :
            answer += 1
            right -= 1
        else :
            answer += 1
            left += 1
            right -= 1

    answer += sum(divmod(len(people[left:right+1]), 2))

    return answer

people, limit = [70, 50, 80, 50], 100
print(solution(people, limit))

people, limit = [70, 80, 50], 100
print(solution(people, limit))

people, limit = [10, 20, 30, 40, 2], 100
print(solution(people, limit))

people, limit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 100
print(solution(people, limit))
