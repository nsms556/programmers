# 2019 카카오 개발자 겨울 인턴십 > 튜플
# https://programmers.co.kr/learn/courses/30/lessons/64065

import re

def solution(s):
    answer = []

    l = sorted(map(lambda x : x[1:-1].split(','), re.findall(r'{.+?}', s[1:-1])), key = lambda x : len(x))

    for i in l :
        for j in i :
            if int(j) not in answer :
                answer.append(int(j))

    return answer

from collections import Counter

def solution(s) :
    answer = []

    s = Counter(re.findall('\d+', s))

    for c, i in s.most_common(len(s)) :
        answer.append(int(c))

    return answer

s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
print(solution(s))

s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
print(solution(s))

s = "{{20,111},{111}}"
print(solution(s))

s = "{{123}}"
print(solution(s))

s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
print(solution(s))
