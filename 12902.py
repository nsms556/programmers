# 연습문제 > 3 x n 타일링
# https://programmers.co.kr/learn/courses/30/lessons/12902

def solution(n):
    answer = 0

    tile = [0, 3]

    for i in range(2, int(n // 2)+1) :
        tile.append((tile[i-1] * 3 + 2) % 1000000007)

        for j in range(i-1) :
            tile[i] = (tile[i] + tile[j] * 2) % 1000000007 

    answer = tile[-1]
    
    return answer

n = 4
print(solution(n))

n = 6
print(solution(n))

n = 8
print(solution(n))

'''
1   2   3   3
2   4   3 * 3 + 2   11
3   6   (3 * 3 + 2) * 3 + 8     41
4   8   ((3 * 3 + 2) * 3 + 8) * 3 + 30  153
5   10  (((3 * 3 + 2) * 3 + 8) * 3 + 30) * 3 + 112 571

'''