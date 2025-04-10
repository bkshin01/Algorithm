def solution(before, after):
    dic = {}
    for ch in before:
        dic[ch] = dic.get(ch, 0) + 1
    for ch in after:
        if ch in dic:
            dic[ch] -= 1
        else:
            return 0
    for v in dic.values():
        if v > 0:
            return 0
    return 1