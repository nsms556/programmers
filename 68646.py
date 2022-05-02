# 월간 코드 챌린지 시즌1 > 풍선 터트리기
# https://programmers.co.kr/learn/courses/30/lessons/68646
# https://programmers.co.kr/questions/13657

def solution(a):
    answer = 1

    left = 0
    right = len(a) - 1

    while left != right :
        #print(left, right)
        if a[left] < a[right] :
            r_search = right - 1
            while a[right] < a[r_search] :
                #print(a[r_search], a[right])
                r_search -= 1
            else :
                right = r_search
                answer += 1
        else :
            l_search = left + 1
            while a[left] < a[l_search] :
                #print(a[left], a[l_search])
                l_search += 1
            else :
                left = l_search
                answer += 1

    return answer

a = [9,-1,-5]
print(solution(a))

a = [-16,27,65,-2,58,-92,-71,-68,-61,-33]
print(solution(a))

'''
-16,27,65,-2,58,-92,-71,-68,-61,-33
-16 -33

-16,65,-2,58,-92,-71,-68,-61,-33
-16 -33

-16,-2,58,-92,-71,-68,-61,-33
-16 -33

-16,58,-92,-71,-68,-61,-33
-16 -33

-16,-92,-71,-68,-61,-33
-92 -33
-92 -61
-92 -68
-92 -71

'''