# 1108 월간 코드 챌린지 시즌2 음양 더하기
# https://programmers.co.kr/learn/courses/30/lessons/76501

def solution(absolutes, signs):
    sign = {True:1, False:-1}

    return sum([i*sign[j] for i,j in zip(absolutes, signs)])

absolutes, signs = [4,7,12], [True,False,True]
print(solution(absolutes, signs))

absolutes, signs = [1,2,3], [False,False,True]
print(solution(absolutes, signs))