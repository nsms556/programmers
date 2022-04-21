# Summer/Winter Coding(~2018) > 기지국 설치
# https://programmers.co.kr/learn/courses/30/lessons/12979

from math import ceil

def solution(n, stations, w):
    answer = 0

    sig_range = 2 * w + 1

    fake_end = n + 1
    not_reach = 1

    for s in stations :
        reach_s = max(1, s-w)

        answer += ceil((reach_s - not_reach) / sig_range)

        not_reach = min(s+w, n) + 1

    answer += ceil((fake_end - not_reach) / sig_range)

    return answer

N, stations, W = 11, [4, 11], 1
print(solution(N, stations, W))

N, stations, W = 16, [9], 2
print(solution(N, stations, W))
