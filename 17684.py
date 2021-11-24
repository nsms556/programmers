# 2018 KAKAO BLIND RECRUITMENT > [3차] 압축
# https://programmers.co.kr/learn/courses/30/lessons/17684

def solution(msg):
    zip_dict = {c:i+1 for i, c in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}
    
    answer = []
    
    l = len(msg)
    while len(msg) :
        if msg[:l] in zip_dict :
            answer.append(zip_dict[msg[:l]])
            
            if len(msg[l:]) > 0 :
                zip_dict[msg[:l+1]] = len(zip_dict)+1

            msg = msg[l:]
            l = len(msg)
        else :
            l -= 1

    return answer

msg = 'KAKAO'
print(solution(msg))

msg = 'TOBEORNOTTOBEORTOBEORNOT'
print(solution(msg))

msg = 'ABABABABABABABAB'
print(solution(msg))
