# 2018 KAKAO BLIND RECRUITMENT > [1차] 캐시
# https://programmers.co.kr/learn/courses/30/lessons/17680

def solution(cacheSize, cities):
    answer = 0

    cache = []

    for c in cities :
        c = c.lower()

        if cacheSize == 0 :
            answer += 5
            continue

        if c in cache :
            answer += 1
            cache.remove(c)
            cache.append(c)
        else :
            if len(cache) < cacheSize :
                cache.append(c)
            else :
                cache.pop(0)
                cache.append(c)
            answer += 5
                
    return answer

from collections import deque

def solution(cacheSize, cities) :
    answer = 0

    cache = deque(maxlen=cacheSize)

    for c in cities :
        c = c.lower()

        if c in cache :
            cache.remove(c)
            cache.append(c)
            answer += 1
        else :
            cache.append(c)
            answer += 5

    return answer

cacheSize, cities = 3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
print(solution(cacheSize, cities))

cacheSize, cities = 3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
print(solution(cacheSize, cities))

cacheSize, cities = 2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
print(solution(cacheSize, cities))

cacheSize, cities = 5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
print(solution(cacheSize, cities))

cacheSize, cities = 2, ["Jeju", "Pangyo", "NewYork", "newyork"]
print(solution(cacheSize, cities))

cacheSize, cities = 0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
print(solution(cacheSize, cities))