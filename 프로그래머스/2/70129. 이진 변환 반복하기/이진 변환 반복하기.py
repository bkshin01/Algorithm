def solution(s):
    answer = [0, 0]
    while int(s) > 1:
        answer[0] += 1
        p1 = ''
        for ch in s:
            if ch == '1':
                p1 += '1'
            else:
                answer[1] += 1
        p2 = bin(len(p1))[2:]
        s = p2
    return answer