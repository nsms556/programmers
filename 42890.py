# 2019 KAKAO BLIND RECRUITMENT > 후보키
# https://programmers.co.kr/learn/courses/30/lessons/42890

from itertools import combinations

def rotate(a) :
    return [list(i) for i in zip(*a)]

def solution(relation):
    answer = 0

    atts = len(relation[0])
    relation = rotate(relation)

    testbed = []
    for i in range(atts) :
        testbed.extend(list(combinations(range(atts), i+1)))

    uniq = []
    for c in testbed :
        t1 = list(zip(*[relation[i] for i in c]))
        t2 = set(t1)

        if len(t1) == len(t2) :
            uniq.append(c)

    for i in uniq :
        if sum(map(set(i).issuperset, uniq)) == 1 :
            answer += 1

    return answer

relation = [["100","ryan","music","2"],["200","apeach","math","2"],
            ["300","tube","computer","3"],["400","con","computer","4"],
            ["500","muzi","music","3"],["600","apeach","music","2"]]
print(solution(relation))
