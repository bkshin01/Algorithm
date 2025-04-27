def solution(want, number, discount):
    answer = 0
    want_dic = {}
    for w, num in zip(want, number):
        want_dic[w] = num
    
    for i in range(len(discount)-9):
        tmp_want_dic = want_dic.copy()
        for j in range(i, i+10):
            cur = discount[j]
            if cur in tmp_want_dic and tmp_want_dic[cur] != 0:
                tmp_want_dic[cur] -= 1
            else:
                break
        if sum(tmp_want_dic.values()) == 0:
            answer += 1
    
    return answer