# 연습문제 > 가장 긴 팰린드롬
# https://programmers.co.kr/learn/courses/30/lessons/12904

def palin2(s) :
    return s == s[::-1]

def solution(s):
    answer = 1

    l = len(s)

    for start in range(l) :
        for end in range(start+2, l+1) :
            ss = s[start:end]

            if palin2(ss) :
                answer = max(answer, len(ss))

    return answer

s = "abcdcba"
print(solution(s))

s = "abacde"
print(solution(s))

s = "abssbac"
print(solution(s))

s = "ac"
print(solution(s))
