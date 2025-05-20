def solution(s):
    dic = {}
    idx = 0
    n = len(s)
    
    while idx < n:
        if s[idx].isdigit():
            tmp = ''
            while s[idx].isdigit():
                tmp += s[idx]
                idx += 1
            dic[tmp] = dic.get(tmp, 0) + 1
        idx += 1
    
    return [int(k) for k, v in sorted(dic.items(), key=lambda x:x[1], reverse=True)]