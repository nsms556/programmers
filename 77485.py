# 2021 Dev-Matching: 웹 백엔드 개발자(상반기) > 행렬 테두리 회전하기
# https://programmers.co.kr/learn/courses/30/lessons/77485

def rotate_border(arr) :
    r = len(arr)

    ret = []
    m = 10001

    for i in range(r) :
        if i == 0 :
            tmp = [arr[i+1][0]] + arr[i][:-1]
            m = min(m, *tmp)
        elif i == r-1 :
            tmp = arr[i][1:] + [arr[i-1][-1]]
            m = min(m, *tmp)
        else :
            tmp = [arr[i+1][0]] + arr[i][1:-1] + [arr[i-1][-1]]
            m = min(m, arr[i+1][0], arr[i-1][-1])
        
        ret.append(tmp)

    return ret, m

def slice_2d(arr, x1, y1, x2, y2) :
    return [row[y1-1:y2] for row in arr[x1-1:x2]]

def replace_2d(arr, repl, x1,y1,x2,y2) :
    for i, x in enumerate(range(x1-1, x2)) :
        arr[x][y1-1:y2] = repl[i]

    return arr

def solution(rows, columns, queries):
    answer = []
    
    arr = [[i*columns + j+1 for j in range(columns)] for i in range(rows)]

    for query in queries :
        x1,y1,x2,y2 = query
        rep, m = rotate_border(slice_2d(arr, x1,y1,x2,y2))
        
        arr = replace_2d(arr, rep, x1,y1,x2,y2)
        answer.append(m)

    return answer

rows, columns, queries = 6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
print(solution(rows, columns, queries))

rows, columns, queries = 3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]
print(solution(rows, columns, queries))

rows, columns, queries = 100, 97, [[1,1,100,97]]
print(solution(rows, columns, queries))

rows, columns, queries = 3, 4, [[1, 1, 2, 2], [1, 2, 2, 3], [1, 3, 2, 4], [2, 3, 3, 4]]
print(solution(rows, columns, queries))

rows, columns, queries = 3, 5, [[1, 1, 2, 2], [2, 3, 3, 4], [1, 2, 3, 4], [1, 1, 3, 4], [2, 2, 3, 5]]
print(solution(rows, columns, queries))

'''
0,0   0,1   ... 0,y-1   0,y
1,0   1,1   ... 1,y-1   1,y
...   ...       ...     ...
x-1,0 x-1,1 ... x-1,y-1 x-1,y
x,0   x,1   ... x,y-1   x,y

1,0 0,0 0,1
2,0 1,1 0,2
3,0 2,1 1,2
3,1 3,2 2,2
'''