def solution(lines):
    answer = 0
    line = [0 for _ in range(200)]
    for s, e in lines:
        for i in range(s, e):
            line[i+100] += 1
    for i in line:
        if i>=2:
            answer += 1
    return answer