# 깊이/너비 우선 탐색(DFS/BFS) > 타겟 넘버
# https://programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    answer = 0

    l = len(numbers)

    def find_target(ops, result) :
        nonlocal answer

        if ops[-1] == '+' :
            result += numbers[len(ops)-1]
        else :
            result -= numbers[len(ops)-1]

        if len(ops) < l :
            ops.append('+')
            find_target(ops, result)
            ops.pop()
            ops.append('-')
            find_target(ops, result)
            ops.pop()
        elif len(ops) > l :
            return
        else :
            if result == target :
                answer += 1
                return ops
            else :
                return

    find_target(['+'], 0)
    find_target(['-'], 0)
               
    return answer

numbers, target = [1, 1, 1, 1, 1], 3
print(solution(numbers, target))

numbers, target = [4,1,2,1], 4
print(solution(numbers, target))
