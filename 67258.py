from collections import defaultdict

def solution(gems):
    answer = []

    needs = set(gems)
    needs_l = len(needs)
    longest = len(gems)
        
    yeogi = 0

    hands_count = defaultdict(int)
    
    for jeogi, gem in enumerate(gems) :
        hands_count[gem] += 1
        
        while len(hands_count) == needs_l :
            hands_count[gems[yeogi]] -= 1
            if hands_count[gems[yeogi]] == 0 :
                del hands_count[gems[yeogi]]
            yeogi +=1

            answer.append([yeogi, jeogi+1])

    answer = min(answer, key=lambda x : (x[1] - x[0], x[0]))
    
    return answer

gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(gems))

gems = ["AA", "AB", "AC", "AA", "AC"]
print(solution(gems))

gems = ["XYZ", "XYZ", "XYZ"]
print(solution(gems))

gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
print(solution(gems))

gems = ["A", "A", "B"] # [2, 3]
print(solution(gems))