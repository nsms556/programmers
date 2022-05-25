# 2021 Dev-Matching: 웹 백엔드 개발자(상반기) > 다단계 칫솔 판매
# https://programmers.co.kr/learn/courses/30/lessons/77486

def solution(enroll, referral, seller, amount):
    ktop = {kid:parent for kid, parent in zip(enroll, referral)}
    money = {p:[] for p in enroll}      

    for s, a in zip(seller, amount) :
        money[s].append(a * 100)

        while s != '-' :
            p = ktop[s]

            if money[s][-1] >= 10 :
                p10 = money[s][-1] // 10

                if p != '-' :
                    money[p].append(p10)

                money[s].append(-p10)
            else :
                break

            s = p

    answer = [sum(i) for i in money.values()]

    return answer

enroll, referral, seller, amount = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]
print(solution(enroll, referral, seller, amount))

enroll, referral, seller, amount = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["sam", "emily", "jaimie", "edward"], [2, 3, 5, 4]
print(solution(enroll, referral, seller, amount))

enroll, referral, seller, amount = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["sam", "emily", "jaimie", "emily"], [2, 3, 5, 4]
print(solution(enroll, referral, seller, amount))
