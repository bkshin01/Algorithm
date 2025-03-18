def solution(genres, plays):
    answer = []
    dic1={}
    dic2={}
    
    for i, (g, p) in enumerate(zip(genres, plays)):
        dic1[g] = dic1.get(g, []) + [(i, p)]
        dic2[g] = dic2.get(g, 0) + p
    
    for (k, v) in sorted(dic2.items(), key=lambda x:x[1], reverse=True):
        for (i, p) in sorted(dic1[k], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(i)
    return answer