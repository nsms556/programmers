# 1018 이상한 문자 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12930

def solution(s):
    new_words = []
    words = list(s.split(' ', -1))

    for word in words :
        new_word = ''
        for i, c in enumerate(list(word)) :
            if i % 2 == 0 :
                new_word += c.upper()
            else :
                new_word += c.lower()

        new_words.append(new_word)

    return ' '.join(new_words)

s = 'try hello world'
print(solution(s))

s = 'try programmers'
print(solution(s))

s = 'Tree'
print(solution(s))

s = 'hello world    t'
print(solution(s))

s = "try hello world strys try t"
print(solution(s))
