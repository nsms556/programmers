# 1022 2018 KAKAO BLIND RECRUITMENT [1차] 다트 게임
# https://programmers.co.kr/learn/courses/30/lessons/17682

import re

def solution(dartResult):
    darts = list(filter(None, re.split('([0-9Z][SDT][*#]?)',  dartResult.replace('10', 'Z'))))

    muities = {'S':1, 'D':2, 'T':3}

    scores = []
    for i, dart in enumerate(darts) :
        scores.append(int(dart[0].replace('Z', '10')) ** muities[dart[1]])

        if len(dart) == 3 :
            if dart[2] == '*' :
                scores[i] *= 2
                if i != 0 :
                    scores[i-1] *= 2
            elif dart[2] == '#' :
                scores[i] *= -1

    return sum(scores)

dartResult = '1S2D*3T'
print(solution(dartResult))

dartResult = '1D2S#10S'
print(solution(dartResult))

dartResult = '1D2S0T'
print(solution(dartResult))

dartResult = '1S*2T*3S'
print(solution(dartResult))

dartResult = '1D#2S*3S'
print(solution(dartResult))

dartResult = '1T2D3D#'
print(solution(dartResult))

dartResult = '1D2S3T*'
print(solution(dartResult))
