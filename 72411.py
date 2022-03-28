# 2021 KAKAO BLIND RECRUITMENT > 메뉴 리뉴얼
# https://programmers.co.kr/learn/courses/30/lessons/72411

def include(order, c) :
    for f in c :
        if f not in order :
            return False
    return True

def include_count(orders, c) :
    return sum(map(lambda x : include(x, c), orders))

def make_course(courses, foods, new_length) :
    new_courses = set()

    for c in courses :
        for f in foods :
            new_c = set(c)
            new_c.add(f)

            if len(new_c) == new_length :
                new_courses.add(tuple(sorted(new_c)))
        
    return new_courses

def solution(orders, course):
    answer = []

    course_count = [dict() for _ in range(max(course))]
    
    for order in orders :
        for food in order :
            course_count[0][food] = course_count[0].get(food, 0) + 1
            
    for c_len in range(2, max(course)+1) :
        for c in make_course(course_count[c_len-2], course_count[0], c_len) :
            cnt = include_count(orders, c)
            if cnt >= 2 :
                course_count[c_len-1][c] = cnt

    for c_len in course :
        c_list = course_count[c_len-1]
        if c_list : 
            items = c_list.items()
            most = max(c_list.values())
            for c, v in items :
                if v == most :
                    answer.append(c)
    
    answer = sorted(list(map(''.join, answer)))
    return answer

orders, course = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]
print(solution(orders, course))

orders, course = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]
print(solution(orders, course))

orders, course = ["XYZ", "XWY", "WXA"], [2,3,4]
print(solution(orders, course))
