# 2022 KAKAO BLIND RECRUITMENT > 신고 결과 받기
# https://programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list, report, k):
    answer = []

    reporting = {i:set() for i in id_list}
    reported = {i:set() for i in id_list}

    for r in report :
        reporter, troll = r.split()

        reporting[reporter].add(troll)
        reported[troll].add(reporter)

    banned = [key for key, v in reported.items() if len(v) >= k]

    for i in id_list :
        answer.append(sum(map(lambda x : x in banned, reporting[i])))

    return answer

id_list, report, k = ["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2
print(solution(id_list, report, k))

id_list, report, k = ["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3
print(solution(id_list, report, k))