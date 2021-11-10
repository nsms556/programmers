# 1110 2021 KAKAO BLIND RECRUITMENT > 신규 아이디 추천
# https://programmers.co.kr/learn/courses/30/lessons/72410

import re

def solution(new_id):
    new_id = new_id.lower()
    
    new_id = re.sub('[^a-z0-9-_.]', '', new_id)

    while new_id.find('..') != -1 :
        new_id = new_id.replace('..', '.')

    if new_id[0] == '.' :
        new_id = new_id[1:]

    if len(new_id) > 0 :
        if new_id[-1] == '.' :
            new_id = new_id[:-1]
    
    if len(new_id) == 0 :
        new_id = 'a'

    if len(new_id) > 15 :
        new_id = new_id[:15]

        if new_id[0] == '.' :
            new_id = new_id[1:]
        if new_id[-1] == '.' :
            new_id = new_id[:-1]

    while len(new_id) <= 2 :
        new_id += new_id[-1]

    return new_id

new_id = "...!@BaT#*..y.abcdefghijklm"
print(solution(new_id))

new_id = "z-+.^."
print(solution(new_id))

new_id = "=.="
print(solution(new_id))

new_id = "123_.def"
print(solution(new_id))

new_id = "abcdefghijklmn.p"
print(solution(new_id))