# 1108 2020 카카오 인턴십 키패드 누르기
# https://programmers.co.kr/learn/courses/30/lessons/67256

def distance(now, next) :
    dist = abs(int((next-1) / 3) - int((now-1) / 3)) 
    if now in [1,3,4,6,7,9,10,12] :
        dist += 1

    return dist

def solution(numbers, hand):
    answer = ''
    left = 10
    right = 12

    for i in numbers :
        if i == 0 :
            i = 11

        #print(left, i, right)

        if i in [1,4,7] :
            answer += 'L'
            left = i
        elif i in [3,6,9] :
            answer += 'R'
            right = i
        else :
            l_dist = distance(left, i)
            r_dist = distance(right, i)
            #print(l_dist, r_dist)

            if l_dist > r_dist :
                right = i
                answer += 'R'
            elif l_dist < r_dist :
                left = i
                answer += 'L'
            else :
                if hand =='left' :
                    left = i
                    answer += 'L'
                else :
                    right = i
                    answer += 'R'

        #print(answer)
    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = 'right'
print(solution(numbers, hand))

numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = 'left'
print(solution(numbers, hand))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
hand = 'right'
print(solution(numbers, hand))
