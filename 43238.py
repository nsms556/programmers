# 이분탐색 > 입국심사
# https://programmers.co.kr/learn/courses/30/lessons/43238

def solution(n, times):
    answer = 0

    def count_people(t) :
        p = 0

        for t in times :
            p += middle // t

        return p

    low, high = 1, max(times) * n

    while low < high :
        middle = (low + high) // 2
        
        p = count_people(middle)

        if n <= p :
            high = middle
        else :
            low = middle + 1

    return low

n, times = 6, [7, 10]
print(solution(n, times))