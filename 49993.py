# Summer/Winter Coding(~2018) > 스킬트리
# https://programmers.co.kr/learn/courses/30/lessons/49993

def solution(skill, skill_trees):
    answer = len(skill_trees)

    prior = {}
    for i, s in enumerate(skill[1:]) :
        prior[s] = skill[i]
    
    for t in skill_trees :
        learn = {s:0 for s in t}
        for s in t :
            if s not in prior :
                learn[s] += 1
            else :
                if prior[s] not in learn :
                    answer -= 1
                    break
                elif learn[prior[s]] == 0 :
                    answer -= 1
                    break
                else :
                    learn[s] += 1
        
    return answer

skill, skill_trees = "CBD", ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_trees))