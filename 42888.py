# 2019 KAKAO BLIND RECRUITMENT > 오픈채팅방
# https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = []
    
    messages = {'Enter':'{}님이 들어왔습니다.', 'Leave':'{}님이 나갔습니다.'}
    users = {}
    logs = []

    for r in record :
        c = r.split()
        
        if c[0] == 'Enter' or c[0] == 'Change' :
            users[c[1]] = c[2]

        if c[0] == 'Enter' or c[0] == 'Leave' :
            logs.append((c[0], c[1]))

    for state, uid in logs :
        answer.append(messages[state].format(users[uid]))

    return answer


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))