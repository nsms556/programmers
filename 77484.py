# 1110 2021 Dev-Matching: 웹 백엔드 개발자(상반기) > 로또의 최고 순위와 최저 순위
# https://programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    correct = [i for i in lottos if i in win_nums]

    print(len(correct), lottos.count(0))

    case1 = 7 - len(correct) if len(correct) else 6
    case2 = 7 - len(correct) - lottos.count(0) if len(correct) + lottos.count(0) else 6

    return [min(case1, case2), max(case1, case2)]

lottos, win_nums = [44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]
print(solution(lottos, win_nums))

lottos, win_nums = [0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]
print(solution(lottos, win_nums))

lottos, win_nums = [45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]
print(solution(lottos, win_nums))

lottos, win_nums = [1,2,3,4,5,6], [20, 9, 8, 45, 12, 35]
print(solution(lottos, win_nums))
