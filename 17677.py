# 2018 KAKAO BLIND RECRUITMENT > [1차] 뉴스 클러스터링
# https://programmers.co.kr/learn/courses/30/lessons/17677

def make_multi_set(s) :
    multi_set = []
    s = s.lower()

    for i in range(len(s)-1) :
        subs = s[i:i+2]

        if subs.isalpha() :
            multi_set.append(subs)

    return multi_set

def solution(str1, str2):
    set1 = make_multi_set(str1)
    set2 = make_multi_set(str2)

    if not (set1 or set2) :
        answer = 1
    else :
        tmp = set1.copy()
        hap = set1.copy()
        for e in set2 :
            if e not in tmp :
                hap.append(e)
            else :
                tmp.remove(e)

        gyo = []
        for e in set2 :
            if e in set1 :
                set1.remove(e)
                gyo.append(e)

        answer = len(gyo) / len(hap)

    return int(answer * 65536)

str1, str2 = 'FRANCE', 'french'
print(solution(str1, str2))

str1, str2 = 'handshake', 'shake hands'
print(solution(str1, str2))

str1, str2 = 'aa1+aa2', 'AAAA12'
print(solution(str1, str2))

str1, str2 = 'E=M*C^2', 'e=m*c^2'
print(solution(str1, str2))
