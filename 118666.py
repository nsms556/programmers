# 2022 KAKAO TECH INTERNSHIP > 성격 유형 검사하기
# https://school.programmers.co.kr/learn/courses/30/lessons/118666

def solution(survey, choices):
    answer = ''

    mbti = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}

    for q, c in zip(survey, choices) :
        c -= 4

        if c > 0 :
            mbti[q[1]] += c
        elif c < 0 :
            mbti[q[0]] += -c

    for q in ['RT', 'CF', 'JM', 'AN'] :
        score1 = mbti[q[0]]
        score2 = mbti[q[1]]

        if score1 >= score2 :
            answer += q[0]
        else :
            answer += q[1]

    return answer

survey, choices = ["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]
print(solution(survey, choices))

survey, choices = ["TR", "RT", "TR"], [7, 1, 3]
print(solution(survey, choices))