# 2020 KAKAO BLIND RECRUITMENT > 문자열 압축
# https://programmers.co.kr/learn/courses/30/lessons/60057

def zipped_string(z) :
    s = ''
    for i in z :
        if i[1] == 1 :
            s += i[0]
        else :
            s += '{}{}'.format(i[1], i[0])

    return s

def zipped_string_length(z, l) :
    length = 0
    for i in z :
        if i[1] == 1 :
            length += len(i[0])
        else :
            length += len(str(i[1])) + l

    return length

def solution(s):
    answer = 1000

    if len(s) == 1:
        return 1
        
    for l in range(1, len(s)//2+1) :
        print(l)
        zipped = []

        for i in range(0, len(s), l) :
            ch = s[i:i+l]

            if not zipped :
                zipped.append([ch, 1])
            elif ch == zipped[-1][0] :
                zipped[-1][1] += 1
            else :
                zipped.append([ch, 1])

        answer = min(answer, zipped_string_length(zipped, l))

    return answer
'''
s = "aabbaccc"
print(solution(s))

s = "ababcdcdababcdcd"
print(solution(s))

s = "abcabcdede"
print(solution(s))

s = "abcabcabcabcdededededede"
print(solution(s))

s = "xababcdcdababcdcd"
print(solution(s))
'''
s = "a"
print(solution(s))
