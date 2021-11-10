# 1110 2021 카카오 채용연계형 인턴십 > 숫자 문자열과 영단어
# https://programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    nums = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4,
            'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}

    for i in nums :
        s = s.replace(i, str(nums[i]))

    return int(s)

s = "one4seveneight"
print(solution(s))

s = "23four5six7"
print(solution(s))

s = "2three45sixseven"
print(solution(s))

s = "123"
print(solution(s))