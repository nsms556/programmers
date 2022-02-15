# 탐욕법(Greedy) > 조이스틱
# https://programmers.co.kr/learn/courses/30/lessons/42860

def solution(name):
    answer = 0
    l = len(name)

    if set(name) == {'A'} :
        return 0

    dic = {}
    for i, c in enumerate('ABCDEFGHIJKLMN') :
        dic[c] = i
    for i, c in enumerate('OPQRSTUVWXYZ') :
        dic[c] = 12 - i

    only_forward = name[:]
    while only_forward[-1] == 'A' :
        only_forward = only_forward[:-1]

    cursor_move = len(only_forward) - 1

    for i, c in enumerate(name) :
        answer += dic[c]

        next_idx = i+1
        while next_idx < l and name[next_idx] == 'A' :
            next_idx += 1

        cursor_move = min(i + i + l - next_idx, cursor_move)
    
    answer += cursor_move
    return answer

def solution(name):
    if set(name) == {'A'} :
        return 0

    cursor_move = 19
    l = len(name)

    for i in range(len(name) // 2) :
        forward = name[-i:] + name[:-i]
        backward = name[i:] + name[:i]

        for n in [forward, backward[0] + backward[:0:-1]] :
            while n and n[-1] == 'A' :
                n = n[:-1]

            cursor_move = min(i + len(n) - 1, cursor_move)

    answer = sum(min(c-65, 91-c) for c in map(ord, name)) + cursor_move
    return answer
'''
name = "JEROEN"
print(solution(name))

name = "JAN"
print(solution(name))

name = "JBAAAN"
print(solution(name))

name = "JBAAABN"
print(solution(name))

name = "JBAABAN"
print(solution(name))

name = "BAABAA"
print(solution(name))

name = "ABAAB"
print(solution(name))

name = "AAABA"
print(solution(name))

name = "ABAAA"
print(solution(name))
'''
name = "ABABAAAAABA"
print(solution(name))

'''
A B C D E F G H I J K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
0 1 2 3 4 5 6 7 8 9 10 11 12 13 12 11 10 9  8  7  6  5  4  3  2  1
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
                                0  1  2  3  4  5  6  7  8  9  10 11
'''