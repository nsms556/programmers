# 1105 해시 완주하지 못한 선수
# https://programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    c = {}
    for p in participant :
        c[p] = c.get(p, 0) + 1

    for p in completion :
        c[p] -= 1

    return [p for p in c if c[p] != 0][0]

participant, completion = ["leo", "kiki", "eden"], ["eden", "kiki"]
print(solution(participant, completion))

participant, completion = ["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]
print(solution(participant, completion))

participant, completion = ["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]
print(solution(participant, completion))