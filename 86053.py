# 월간 코드 챌린지 시즌3 > 금과 은 운반하기
# https://programmers.co.kr/learn/courses/30/lessons/86053
# https://bladejun.tistory.com/166

def solution(a, b, g, s, w, t):
    answer = -1

    high = (1e9 * 2) * (1e5 * 2)
    low = 0

    def item_move_count(time) :
        item_moves = []
        for truck in t :
            way2, way1 = divmod(time // truck, 2)

            item_moves.append(way2 + way1)

        return item_moves
    
    while low <= high :
        mid = int((low + high) // 2)
        gold = 0
        silver = 0
        total = 0

        item_moves = item_move_count(mid)

        for i, move in enumerate(item_moves) :
            city_gold = g[i]
            city_silver = s[i]
            truck_weight = w[i]

            gold += (move * truck_weight) if city_gold >= move * truck_weight else city_gold
            silver += (move * truck_weight) if city_silver >= move * truck_weight else city_silver
            total += (move * truck_weight) if city_gold + city_silver >= move * truck_weight else city_gold + city_silver

        if gold >= a and silver >= b and total >= a + b :
            high = mid - 1
        else :
            low = mid + 1
            
    answer = low

    return answer

a, b, g, s, w, t = 10, 10, [100], [100], [7], [10]
print(solution(a, b, g, s, w, t))

a, b, g, s, w, t = 90, 500, [70,70,0], [0,0,500], [100,100,2], [4,8,1]
print(solution(a, b, g, s, w, t))
