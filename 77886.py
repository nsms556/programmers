# 월간 코드 챌린지 시즌2 > 110 옮기기
# https://programmers.co.kr/learn/courses/30/lessons/77886

def dict_first(s) :
    tmp = ''
    cnt = 0

    for c in s :
        tmp += c

        if tmp[-3:] == '110' :
            cnt += 1
            tmp = tmp[:-3]

    idx = -1
    for i in range(len(tmp)-1, -1, -1) :
        if tmp[i] == '0' :
            idx = i + 1
            break
    else :
        return '110' * cnt + tmp

    s = tmp[:idx] + '110' * cnt + tmp[idx:]

    return s

def solution(s):
    answer = []

    for ss in s :
        answer.append(dict_first(ss))

    return answer

s = ["1110","100111100","0111111010", "1100111011101001"]
print(solution(s))

'''
1100111011101001
0101101101101101
0101101101101101
'''