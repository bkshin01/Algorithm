from collections import deque

def solution(progresses, speeds):
    result = []
    p = deque(progresses)
    s = deque(speeds)
    while p:
        for i in range(len(p)):
            p[i] += s[i]
        if p[0] >= 100:
            cnt = 0
            while p and p[0] >= 100:
                p.popleft()
                s.popleft()
                cnt += 1
            result.append(cnt)
    return result