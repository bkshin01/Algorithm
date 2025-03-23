def solution(s1, s2):
    answer = 0
    dic = {}
    for ch in s1:
        dic[ch] = dic.get(ch, 0) + 1
    for ch in s2:
        if ch in dic:
            answer += 1
    return answer