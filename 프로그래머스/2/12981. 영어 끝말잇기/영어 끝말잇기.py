def solution(n, words):
    dic = {}
    answer = [0, 0]
    
    dic[words[0]] = 1
    last_ch = words[0][-1]
    
    for i in range(1, len(words)):
        cur = words[i]
        if cur not in dic and cur[0] == last_ch:
            dic[cur] = 1
            last_ch = cur[-1]
        else:
            answer[0] = (i%n) + 1
            answer[1] = (i//n) + 1
            break
    return answer