# 해시 > 위장
# https://programmers.co.kr/learn/courses/30/lessons/42578

from math import prod

def solution(clothes):
    new_clothes = {}

    for cl, cat in clothes :
        new_clothes[cat] = new_clothes.get(cat, set(['']))
        new_clothes[cat].add(cl)

    answer = prod(map(len, new_clothes.values())) - 1

    return answer

from collections import Counter
from functools import reduce

def solution(clothes) :
    clothes = Counter([cat for name, cat in clothes])

    answer = reduce(lambda x,y : x*(y+1), clothes.values(), 1) - 1

    return answer

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))

clothes = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
print(solution(clothes))

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["smoky_makeup", "face"]]
print(solution(clothes))
