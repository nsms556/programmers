# 자물쇠와 열쇠
# https://programmers.co.kr/learn/courses/30/lessons/60059

from collections import deque

def clockwise(x) :
    return list(zip(*x[::-1]))

def reversal(array) :
    def toggle(row) :
        return list(map(lambda x : x ^ 1, row))

    return list(map(toggle, array)) 

def replace_2d(array, repl, x1, y1, x2) :
    y = y1
    
    for row in repl :
        array[y][x1:x2] = row
        y += 1

    return array

def print_2d(array) :
    for r in array :
        print(r)

def shift(array, direction, distance=1) :
    if direction == 'D' :
        array = deque(array)
        array.rotate(distance)
        array = list(array)

    elif direction == 'R' :
        array = list(map(deque, array))

        for i in range(len(array)) :
            array[i].rotate(distance)

        array = list(map(list, array))

    return array

def key_extend(key, new_size) :
    new_key = [[0 for _ in range(new_size)] for _ in range(new_size)]
    new_key = replace_2d(new_key, key, 0, 0, len(key))
    
    return new_key

def try_unlock(key, lock, x, y, o_size) :
    k = [r[y:y+o_size] for r in key[x:x+o_size]]

    print(k)

    return k == lock

def solution(key, lock):
    answer = False

    keys = []
    for _ in range(4) :
        key = clockwise(key)
        keys.append(key)

    lock = reversal(lock)
    n = len(lock)
    m = len(key)

    ex_m = n + 2*(m-1)
    
    keys = list(map(key_extend, keys, [ex_m] * 4))

    flag = False

    for k in keys :
        for y in range(ex_m - m + 1) :
            kk = shift(k, 'D', y)

            for x in range(ex_m - m + 1) :
                kkk = shift(kk, 'R', x)
                '''print_2d(kkk)
                print()'''

                if try_unlock(kkk, lock, m-1, m-1, n) :
                    answer = True
                    flag = True
                    break

            if flag :
                break

        if flag :
            break

    return answer
'''
key, lock = [[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))

key, lock = [[1,1,1], [1,1,1], [1,1,1]], [[0,0,0], [0,0,0], [0,0,0]]
print(solution(key, lock))

key, lock = [[0,0,0], [0,0,0], [0,0,0]], [[1,1,1], [1,1,1], [1,1,1]]
print(solution(key, lock))

key, lock = [[0,0,1], [0,0,0], [0,0,0]], [[1,1,1], [1,1,1], [1,1,1]]
print(solution(key, lock))
'''
key, lock = [[0,0,1], [0,0,0], [0,0,0]], [[1,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1]]
print(solution(key, lock))