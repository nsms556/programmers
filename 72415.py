# 2021 KAKAO BLIND RECRUITMENT > 카드 짝 맞추기
# https://programmers.co.kr/learn/courses/30/lessons/72415
# https://tiktaek.tistory.com/68

from collections import defaultdict, deque
from copy import deepcopy
from itertools import permutations


def print_2d(arr) :
    for r in arr :
        print(r)

def solution(board, r, c):
    answer = float('inf')

    n = 4
    cursor = (r, c)
    enter_cnt = sum(sum(map(lambda x : x != 0, row)) for row in board)
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    cards = defaultdict(list)

    for y in range(n) :
        for x in range(n) :
            if board[y][x] != 0 :
                cards[board[y][x]].append((y, x))

    def move_min(board, start, end) :
        if start == end :
            return 0

        queue = deque()
        visited = {start}
        queue.append((start[0], start[1], 0))

        while queue :
            y, x, cost = queue.popleft()

            for dy, dx in dirs :
                new_y, new_x = y + dy, x + dx
                ctrl_y, ctrl_x = y, x

                while True :
                    ctrl_y, ctrl_x = ctrl_y + dy, ctrl_x + dx

                    if not (0 <= ctrl_y < 4 and 0 <= ctrl_x < 4) :
                        ctrl_y, ctrl_x = ctrl_y - dy, ctrl_x - dx
                        break
                    elif board[ctrl_y][ctrl_x] != 0 :
                        break

                if (new_y, new_x) == end or (ctrl_y, ctrl_x) == end :
                    return cost + 1

                if (0 <= new_y < 4 and 0 <= new_x < 4) and (new_y, new_x) not in visited :
                    queue.append((new_y, new_x, cost+1))
                    visited.add((new_y, new_x))
                if (ctrl_y, ctrl_x) not in visited :
                    queue.append((ctrl_y, ctrl_x, cost+1))
                    visited.add((ctrl_y, ctrl_x))

    def find_min_cost(board, cursor, order, cost) :
        if not order :
            return cost

        a_card, b_card = cards[order[0]]
        cost_a = move_min(board, cursor, a_card) + move_min(board, a_card, b_card)
        cost_b = move_min(board, cursor, b_card) + move_min(board, b_card, a_card)

        new_board = deepcopy(board)
        new_board[a_card[0]][a_card[1]] = 0
        new_board[b_card[0]][b_card[1]] = 0

        if cost_a < cost_b :
            return find_min_cost(new_board, b_card, order[1:], cost + cost_a)
        else :
            return find_min_cost(new_board, a_card, order[1:], cost + cost_b)

    for c_order in permutations(cards.keys(), len(cards)) :
        answer = min(answer, find_min_cost(board, cursor, c_order, 0))

    answer += enter_cnt

    return answer

board, r, c = [[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1, 0
print(solution(board, r, c))

board, r, c = [[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]], 0, 1
print(solution(board, r, c))
