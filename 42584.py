# 스택/큐 > 주식가격
# https://programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    answer = []
    
    for i in range(len(prices)) :
        cnt = 0

        for j in range(i+1, len(prices)) :
            cnt += 1

            if prices[j] < prices[i] :
                break

        answer.append(cnt)

    return answer

def solution(prices) :
    answer = [0] * len(prices)

    stack = [0]

    for i in range(1, len(prices)) :
        print(stack)
        if prices[i] < prices[stack[-1]] :
            for j in stack[::-1] :
                if prices[i] < prices[j] :
                    answer[j] = i - j
                    stack.remove(j)
                    print(stack)
                else :
                    break

        stack.append(i)
    
    print(answer)
    for i in range(len(stack)-1) :
        answer[stack[i]] = len(prices) - stack[i] - 1

    return answer

prices = [1, 2, 3, 2, 3]
print(solution(prices))

prices = [5, 6, 4, 8, 6]
print(solution(prices))