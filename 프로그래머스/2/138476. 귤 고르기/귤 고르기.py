def solution(k, tangerine):
    answer = 0
    dic = {}
    for t in tangerine:
        dic[t] = dic.get(t, 0) + 1
    sorted_d = dict(sorted(dic.items(), key=lambda x:x[1], reverse=True))
    for i in sorted_d:
        if k <= 0:
            return answer
        k -= sorted_d[i]
        answer += 1
    return answer