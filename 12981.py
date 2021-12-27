# Summer/Winter Coding(~2018) > 영어 끝말잇기
# https://programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    answer = [0, 0]

    exist = []
    prev = None

    for i, w in enumerate(words) :
        if prev == None :
            exist.append(w)
        elif w in exist or prev[-1] != w[0] :
            answer = [i % n + 1, i // n + 1]
            break
        else :
            exist.append(w)

        prev = w

    return answer

n, words = 3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
print(solution(n, words))

n, words = 5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]
print(solution(n, words))

n, words = 2, ["hello", "one", "even", "never", "now", "world", "draw"]
print(solution(n, words))