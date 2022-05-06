# 깊이/너비 우선 탐색(DFS/BFS) > 단어 변환
# https://programmers.co.kr/learn/courses/30/lessons/43163

from collections import defaultdict, deque

def solution(begin, target, words):
    answer = 0

    if target not in words :
        return answer

    graph = defaultdict(list)

    for w in [begin] + words :
        for ww in words :
            if sum([c != cc for c, cc in zip(w, ww)]) == 1 :
                graph[w].append(ww)

    queue = deque()
    queue.append((begin, 0))

    history = []

    while queue :
        word, answer = queue.popleft()

        history.append(word)

        if word == target :
            break

        for n_word in graph[word] :
            if n_word not in history and n_word not in queue :
                queue.append((n_word, answer + 1))

    if word != target :
        answer = 0

    return answer

begin, target, words = "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))

begin, target, words = "hit", "cog", ["hot", "dot", "dog", "lot", "log"]
print(solution(begin, target, words))

begin, target, words = "hit", "cog", ["dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))

begin, target, words = "aab", "aba", ["abb", "aba"]
print(solution(begin, target, words))