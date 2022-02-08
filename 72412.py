# 2021 KAKAO BLIND RECRUITMENT > 순위 검색
# https://programmers.co.kr/learn/courses/30/lessons/72412

def querying(data, query) :
    for i, item in enumerate(zip(data, query)) :
        if i == 4 :
            if int(item[0]) < int(item[1]) :
                return None
        else :
            if not (item[1] == '-' or item[0] == item[1]) :
                return None

    return data

def solution(info, query):
    answer = []

    info = list(map(lambda x : x.split(), info))
    query = list(map(lambda x : x.replace('and', '').split(), query))

    for q in query :
        q_answer = list(map(lambda x : querying(x, q), info))
        q_answer = [a for a in q_answer if a != None]
        answer.append(len(q_answer))

    return answer

from itertools import product
from bisect import bisect_left

def bin_search(l, item) :
    start = 0
    end = len(l)

    while start < end :
        mid = (start + end) // 2

        if item <= l[mid] :
            end = mid
        else :
            start = mid + 1

    return start

def solution(info, query) :
    answer = []

    info = sorted(list(map(lambda x : x.split(), info)), key=lambda x : int(x[4]))

    table = {}
    for i in info :
        lang, cat, career, food = ['-'], ['-'], ['-'], ['-']
        
        lang.append(i[0])
        cat.append(i[1])
        career.append(i[2])
        food.append(i[3])
        score = i[4]

        for k in list(product(lang, cat, career, food)) :
            k = ''.join(k)
            table[k] = table.get(k, [])
            table[k].append(int(score))

    for q in query :
        q = list(q.replace('and', '').split())
        q_score = int(q[4])
        q_k = ''.join(q[:4])

        q_answer = table.get(q_k, [])
        if q_answer :
            answer.append(len(q_answer) - bisect_left(q_answer, q_score))
        else :
            answer.append(0)
        
    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))
