# Summer/Winter Coding(~2018) > 점프와 순간 이동
# https://programmers.co.kr/learn/courses/30/lessons/12980

def solution(n):
    ans = 0
    
    while n :
        if n % 2 == 0 :
            n //= 2
        else :
            n -= 1
            ans += 1

    return ans

def solution(n) :
    return bin(n).count('1')

n = 5
print(solution(n))

n = 6
print(solution(n))

n = 5000
print(solution(n))
'''
5
0 1 2 3 4 5
1 1 J
2 2 T 
3 4 T
4 5 J

6
0 1 2 3 4 5 6
1 1 J
2 2 T
3 3 J
4 6 T

5000 T
2500 T
1250 T
625 J
624 T
312 T
156 T
78 T
39 J
38 T 
19 J
18 T
9 J
8 T 
4 T
2 T
1 J
'''