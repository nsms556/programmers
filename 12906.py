# 1021 같은 숫자는 싫어
# https://programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    answer = []
    
    answer.append(arr[0])
    for i in arr[1:] :
        if i != answer[-1] :
            answer.append(i)
    
    return answer

arr = [1,1,3,3,0,1,1]
print(solution(arr))

arr = [4,4,4,3,3]
print(solution(arr))