# 연습문제 > 선입 선출 스케줄링
# https://programmers.co.kr/learn/courses/30/lessons/12920
# https://programmers.co.kr/learn/courses/30/lessons/43238

def solution(n, cores):
    answer = 0

    def count_works(time) :
        w = 0

        for c in cores :
            w += time // c

        return w

    n -= len(cores)
    low, high = 1, max(cores) * n

    while low < high :
        middle = (low + high) // 2

        w = count_works(middle)

        if w >= n :
            high = middle
        else :
            low = middle + 1

    for c in cores :
        n -= (high - 1) // c

    for i, core in enumerate(cores) :
        if high % cores[i] == 0 :
            n -= 1

            if n == 0 :
                answer = i + 1
 
    return answer

n, cores = 6, [1,2,3]
print(solution(n, cores))

''' 
  1 2 3
0 1 2 3
1 4 2 3 
2 5 6 3 
3 x 6 x 
4 
5
6
'''