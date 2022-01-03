# 2018 KAKAO BLIND RECRUITMENT > [1차] 프렌즈4블록
# https://programmers.co.kr/learn/courses/30/lessons/17679

def rotate(board) :
    return list(map(list, zip(*board[::-1])))

def solution(m, n, board):
    answer = 0
    board = rotate(list(map(list, board)))

    while True :
        cascade = set()
        for i in range(n-1) :
            for j in range(m-1) :
                o = board[i][j]
                if o == board[i+1][j] and o == board[i][j+1] and o == board[i+1][j+1] and o != 0:
                    cascade.add((i, j))
                    cascade.add((i+1, j))
                    cascade.add((i, j+1))
                    cascade.add((i+1, j+1))

        if cascade :
            print(cascade)
            answer += len(cascade)

            for x, y in cascade :
                board[x][y] = 0
            for i, r in enumerate(board) :
                cnt = r.count(0)
                board[i] = [a for a in r if a != 0] + ([0] * cnt)

            print(board)
        else :
            print(board)
            break

    return answer

m, n, board = 4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]
print(solution(m, n, board))
'''
0     1     2     3
CCBDE CCBDE    DE     E
AAADE    DE    DE     E
AAABF    BF CCBBF    DF
CCBBF CCBBF CCBBF    DF
      6     8     0
[['C',  0,   0,  'D', 'E'], 
 ['A',  0,   0,  'D', 'E'], 
 ['A', 'C', 'B', 'B', 'F'],
 ['C', 'C', 'B', 'B', 'F']]

'''

m, n, board = 6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
print(solution(m, n, board))
'''
0      1      2
TTTANT              
RRFACC    A      A  
RRRFCC T TANT   TANT
TRRRAA TTFFAA   FFAA
TTMMMF TTMMMF T MMMF
TMMTTJ TMMTTJ TMMTTJ
11     4      0
'''

m, n, board = 7, 2, ["AA", "BB", "AA", "BB", "ZZ", "ZZ", "CC"]
print(solution(m, n, board))
'''
0
AA
BB
AA
00
00
BB
CC

'''