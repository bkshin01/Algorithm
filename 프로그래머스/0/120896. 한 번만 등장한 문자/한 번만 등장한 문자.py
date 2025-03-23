def solution(s):
    dic = {}
    for ch in s:
        dic[ch] = dic.get(ch, 0) + 1
    answer = ""
    for k, v in dic.items():
        if v == 1:
            answer += k
    return ''.join(sorted(answer))