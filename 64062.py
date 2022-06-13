# 2019 카카오 개발자 겨울 인턴십 > 징검다리 건너기
# https://programmers.co.kr/learn/courses/30/lessons/64062

def solution(stones, k):
    low, high = 1, 200000000

    while low <= high :
        mid = (low + high) // 2

        cnt = 0
        for stone in stones :
            if stone <= mid :
                cnt += 1

                if cnt >= k :
                    break
            else :
                cnt = 0

        if cnt >= k :
            high = mid - 1
        else :
            low = mid + 1

    answer = low

    return answer

stones, k = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3
print(solution(stones, k))

'''
[0, 0, 0, 5, 5, 4, 5, 2, 4, 5, 2, 4, 5, 3, 2, 1, 4, 2, 5, 1]

'''