# 해시 > 전화번호 목록
# https://programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    answer = True

    phone_book.sort()

    for i in range(len(phone_book)-1) :
        l = len(phone_book[i])
        if phone_book[i] in phone_book[i+1][:l] :
            answer = False
            break

    return answer

phone_book = ["119", "97674223", "1195524421"]
print(solution(phone_book))

phone_book = ["123","456","789"]
print(solution(phone_book))

phone_book = ["12","123","1235","567","88"]
print(solution(phone_book))

phone_book = ['123']
print(solution(phone_book))