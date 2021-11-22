# 2018 KAKAO BLIND RECRUITMENT > [3차] 파일명 정렬
# https://programmers.co.kr/learn/courses/30/lessons/17686

import re

def solution(files):
    p = re.compile(r'(\D+)(\d{1,5})([\d\D]+)?', re.IGNORECASE)
    
    answer = []
    for i in files :
        m = list(p.match(i).groups())
        if m[2] == None :
            m[2] = ''

        answer.append(m)

    #print(answer)

    answer = list(map(''.join, sorted(answer, key=lambda x:(x[0].lower(), int(x[1])))))

    return answer

files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
print(solution(files))

files = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
print(solution(files))

files = ["F-5", "B-50", "A-10", "F-14"]
print(solution(files))

files = ["F-5", "F-50", "f-10", "f-14"]
print(solution(files))

files = ["F-50000scsv", "f-500001asd", "a-100012aaaa", "z-142314cccc"]
print(solution(files))

files = ['a.c01', 'b.d02', 'a.c03', 'a.c89']
print(solution(files))

files = ['a100-psd.bak', 'a102-psd.psd', 'a103-psd.bak','a301-psd.bak', 'a300-psd.bak']
print(solution(files))
