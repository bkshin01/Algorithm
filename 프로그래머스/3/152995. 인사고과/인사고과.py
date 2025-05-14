def solution(scores):
    result = 0
    max_s2 = 0
    
    w1, w2 = scores[0]
    ws = w1 + w2
    scores.sort(key=lambda x: (-x[0], x[1]))
    
    for s1, s2 in scores:
        if w1 < s1 and w2 < s2:
            return -1
        if s2 >= max_s2:
            max_s2 = s2
            if s1 + s2 > ws:
                result += 1
    
    return result + 1