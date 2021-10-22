# 1022 가운데 글자 가져오기
# https://programmers.co.kr/learn/courses/30/lessons/12903

def solution(s):
    l = len(s)
    if l % 2 == 1 :
        answer = s[l // 2]
    else :
        answer = s[l//2-1:l//2+1]
    return answer

s = 'abcde'
print(solution(s))

s = 'qwer'
print(solution(s))