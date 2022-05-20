# 해시 > 베스트앨범
# https://programmers.co.kr/learn/courses/30/lessons/42579

from collections import defaultdict, Counter

def solution(genres, plays):
    answer = []

    genre_count = defaultdict(int)
    songs = defaultdict(list)

    for i, (g, p) in enumerate(zip(genres, plays)) :
        genre_count[g] += p
        songs[g].append((p, i))

    order = [i[0] for i in Counter(genre_count).most_common(len(genre_count))]

    for g in order :
        answer += [i[1] for i in list(sorted(songs[g], key=lambda x : x[0], reverse=True))[:2]]

    return answer

genres, plays = ["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]
print(solution(genres, plays))
