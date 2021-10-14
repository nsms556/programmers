# 직사각형 별찍기
# https://programmers.co.kr/learn/courses/30/lessons/12969

a, b = map(int, input().strip().split(' '))

for j in range(b) :
    for i in range(a) :
        print('*', end='')
    print()