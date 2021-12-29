# 월간 코드 챌린지 시즌2 > 2개 이하로 다른 비트
# https://programmers.co.kr/learn/courses/30/lessons/77885

def solution(numbers):
    answer = []

    for x in numbers :
        y = x + 1

        while True :
            if bin(x ^ y).count('1') <= 2 :
                answer.append(y)
                break
            else :
                y += 1

    return answer

def solution(numbers):
    answer = []

    for x in numbers :
        mod = x % 4

        if mod < 3 :
            answer.append(x+1)
        else :
            b = bin(x)
            if b.count('1') != len(b) - 2 :
                b = b[2:][::-1]
            else :
                b = b[2:] + '0' 

            zero = b.index('0')
            answer.append(x + 2**(zero-1))

    return answer

numbers = [2,7]
print(solution(numbers))

'''
mod = 0
4 -> 100 -> 101 -> 5
8 -> 1000 -> 1001 -> 9
12 -> 1100 -> 1101 -> 13

mod = 1
5 -> 101 -> 110 -> 6
9 -> 1001 -> 1010 -> 10
13 -> 1101 -> 1110 -> 14

mod = 2
6 -> 110 -> 111 -> 7
10 -> 1010 -> 1011 -> 11
14 -> 1110 -> 1111 -> 15

mod = 3
3 -> 011 -> 101 -> 5
7 -> 0111 -> 1011 -> 11
11 -> 1011 -> 1101 -> 13\
15 -> 01111 -> 10111 -> 23
19 -> 10011 -> 10101 -> 21
23 -> 10111 -> 11011 -> 27
27 -> 11011 -> 11101 -> 29
31 -> 011111 -> 101111 -> 47

10111
00011
11011


'''