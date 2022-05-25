# 2019 KAKAO BLIND RECRUITMENT > 매칭 점수
# https://programmers.co.kr/learn/courses/30/lessons/42893

import re

def get_word_score(word, page) :
    score = 0
    word = word.lower()
    p = re.compile('[^a-zA-Z]')
    
    for t in p.sub(' ', page).split() :
        if word == t.lower() :
            score += 1
    
    return score

def get_links(page) :
    return re.findall('<a href="(https://\S+)"', page)

def get_url(page) :
    m = re.search('<meta property="og:url" content="(https://\S+)"', page)
    return m.group(1)

def solution(word, pages):
    answer = 0

    scores = {}
    link_score = {}
    links = {}
    urls = {}
    
    for i, p in enumerate(pages) :
        url = get_url(p)

        urls[url] = i
        scores[url] = get_word_score(word, p)
        links[url] = get_links(p)

        link_score[url] = scores[url] / len(links[url]) if links[url] else 0
    
    for origin, externals in links.items() :
        for ext in externals :
            if ext in scores :
                scores[ext] += link_score[origin]

    answer = sorted(scores.keys(), key=lambda x : scores[x], reverse=True)[0]

    return urls[answer]

word = 'blind'
pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]
print(solution(word, pages))

word = 'Muzi'
pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]
print(solution(word, pages))
