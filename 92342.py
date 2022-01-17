# 2022 KAKAO BLIND RECRUITMENT > 양궁대회
# https://programmers.co.kr/learn/courses/30/lessons/92342

from itertools import combinations_with_replacement
comb = combinations_with_replacement

def calculate_score(a_shoot, r_shoot) :
    a_score = 0
    r_score = 0

    for i, (a, r) in enumerate(zip(a_shoot, r_shoot)) :
        if a == 0 and a == r :
            continue
        elif r <= a :
            a_score += (10 - i)
        else :
            r_score += (10 - i)

    return a_score, r_score

def solution(n, info):
    answer = []

    shoots_avail = set([tuple(i.count(score) for score in range(10, -1, -1)) for i in comb(range(11), n)])

    max_diff = 0
    final_shoots = set()
    for r_shoot in shoots_avail :
        a_score, r_score = calculate_score(info, r_shoot)

        if r_score - a_score > max_diff :
            max_diff = r_score - a_score
            final_shoots = set([r_shoot])
        elif r_score - a_score == max_diff :
            final_shoots.add(r_shoot)

    if max_diff == 0 :
        answer = [-1]
    else :
        answer = list(sorted(final_shoots, key=lambda x : list(reversed(x)), reverse=True)[0])

    return answer

n, info = 5, [2,1,1,1,0,0,0,0,0,0,0]
print(solution(n, info))

n, info = 1, [1,0,0,0,0,0,0,0,0,0,0]
print(solution(n, info))

n, info = 9, [0,0,1,2,0,1,1,1,1,1,1]
print(solution(n, info))

n, info = 10, [0,0,0,0,0,0,0,0,3,4,3]
print(solution(n, info))
