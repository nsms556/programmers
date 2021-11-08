# 1108 2019 카카오 개발자 겨울 인턴십 크레인 인형뽑기 게임
# https://programmers.co.kr/learn/courses/30/lessons/64061

def rotate(x) :
    return list(zip(*x[::-1]))

def solution(board, moves):
    answer = 0

    board = list(map(list, rotate(board)))

    for i in range(len(board)) :
        board[i] = [k for k in board[i] if k > 0]

    pick = []

    for m in moves :
        if len(board[m-1]) > 0 : 
            pick.append(board[m-1].pop())
        else :
            continue
        
        if len(pick) > 1 :
            if pick[-2] == pick[-1] :
                pick.pop()
                pick.pop()
                answer += 2

    return answer

board = [[0,0,0,0,0],
         [0,0,1,0,3],
         [0,2,5,0,1],
         [4,2,4,4,2],
         [3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))
