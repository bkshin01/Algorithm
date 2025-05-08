def solution(enroll, referral, seller, amount):    
    dic = {}
    for i, e in enumerate(enroll):
        dic[e] = i
    
    benefit = [0 for _ in range(len(enroll))]
    for s, a in zip(seller, amount):
        m = a * 100
        while s != "-" and m > 0:
            idx = dic[s]
            benefit[idx] += m - m//10
            m //= 10
            s = referral[idx]
            
    return benefit