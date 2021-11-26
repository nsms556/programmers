# 2018 KAKAO BLIND RECRUITMENT > [3차] 방금그곡
# https://programmers.co.kr/learn/courses/30/lessons/17683

def sharp_replace(s) :
    return s.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')

def solution(m, musicinfos):
    broadcasts = []
    for music in musicinfos :
        start, end, name, scale = music.split(',')
        start_h, start_m = map(int, start.split(':'))
        end_h, end_m = map(int, end.split(':'))

        scale = sharp_replace(scale)

        b_len = (end_h - start_h) * 60 + (end_m - start_m)
        b_scale = scale * (b_len // len(scale)) + scale[:b_len % len(scale)]

        broadcasts.append((name, b_scale))

    m = sharp_replace(m)
    answer = ''
    answer_len = 0
    for b in broadcasts :
        if m in b[1] :
            if answer_len < len(b[1]) :
                answer = b[0]
                answer_len = len(b[1])

    return answer if answer != '' else '(None)'

m, musicinfos = "ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
print(solution(m, musicinfos))

m, musicinfos = "CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
print(solution(m, musicinfos))

m, musicinfos = "ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
print(solution(m, musicinfos))
