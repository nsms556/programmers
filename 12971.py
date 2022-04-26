# Summer/Winter Coding(~2018) > 스티커 모으기(2)
# https://programmers.co.kr/learn/courses/30/lessons/12971
# https://programmers.co.kr/questions/24769

def solution(sticker):
    if len(sticker) == 1 :
        return sticker[0]
        
    start0 = sticker[:-1]
    for i in range(1, len(start0)) :
        if i == 1 :
            start0[i] = max(start0[i], start0[i-1])
        else :
            start0[i] = max(start0[i-1], start0[i-2] + start0[i])

    start1 = sticker[1:]
    for i in range(1, len(start1)) :
        if i == 1 :
            start1[i] = max(start1[i], start1[i-1])
        else :
            start1[i] = max(start1[i-1], start1[i-2] + start1[i])

    return max(start0[-1], start1[-1])

sticker = [14, 6, 5, 11, 3, 9, 2, 10]
print(solution(sticker))

sticker = [1, 3, 2, 5, 4]
print(solution(sticker))
