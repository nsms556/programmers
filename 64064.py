# 2019 카카오 개발자 겨울 인턴십 > 불량 사용자
# https://programmers.co.kr/learn/courses/30/lessons/64064

from itertools import product

def match(pattern, string) :
    if len(pattern) != len(string) :
        return False

    return all(map(lambda x : x[0] == '*' or x[0] == x[1] , zip(pattern, string)))

def solution(user_id, banned_id):
    answer = set()

    matched = []
    for pattern in banned_id :
        matched.append([user for user in user_id if match(pattern, user)])

    banned = set(map(tuple, map(sorted, map(set, product(*matched)))))

    for c in banned :
        if len(c) != len(banned_id) :
            continue

        answer.add(c)

    return len(answer)

user_id, banned_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]
print(solution(user_id, banned_id))

user_id, banned_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]
print(solution(user_id, banned_id))

user_id, banned_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]
print(solution(user_id, banned_id))
