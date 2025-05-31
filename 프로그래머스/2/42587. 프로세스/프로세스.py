from collections import deque

def solution(priorities, location):
    trace = deque([0 for _ in range(len(priorities))])
    trace[location] = 1
    q = deque(priorities)
    cnt = 1
    
    while q:
        cur = q.popleft()
        if q and cur < max(q):
            q.append(cur)
            trace.append(trace.popleft())
        elif trace[0] == 1:
            return cnt
        else:
            trace.popleft()
            cnt += 1