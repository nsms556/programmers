# 1027 2018 KAKAO BLIND RECRUITMENT [1차] 비밀지도
# https://programmers.co.kr/learn/courses/30/lessons/17681

def solution(n, arr1, arr2):
    answer = []

    for m1, m2 in zip(arr1, arr2) :
        answer.append(format(m1 | m2, '{}b'.format(n)).replace('1', '#').replace('0', ' '))

    return answer


n = 5
arr1 = [9,20,28,18,11]
arr2 = [30,1,21,17,28]
print(solution(n, arr1, arr2))

n = 6
arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]
print(solution(n, arr1, arr2))