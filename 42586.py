# 스택/큐 > 기능개발
# https://programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    answer = []

    progresses.reverse()
    speeds.reverse()

    while progresses :
        complete = 0
        
        while progresses and progresses[-1] >= 100 :
            progresses.pop()
            speeds.pop()

            complete += 1
        
        if complete :
            answer.append(complete)

        for i, (p, s) in enumerate(zip(progresses, speeds)) :
            if p < 100 :
               progresses[i] += s

    return answer

progresses, speeds = [93, 30, 55], [1, 30, 5]
print(solution(progresses, speeds))

progresses, speeds = [95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]
print(solution(progresses, speeds))
