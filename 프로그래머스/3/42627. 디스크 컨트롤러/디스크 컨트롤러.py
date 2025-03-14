from collections import deque
from heapq import heappop, heappush

def solution(jobs):
    tasks = deque(sorted([(x[1], x[0]) for x in jobs], key=lambda x: (x[1], x[0])))
    q = []
    heappush(q, tasks.popleft())
    cur, result = 0, 0
    
    while q:
        duration, arrive = heappop(q)
        cur = max(cur+duration, arrive+duration)
        result += (cur - arrive)
        
        while tasks and tasks[0][1] <= cur:
            heappush(q, tasks.popleft())
        
        if tasks and len(q) == 0:
            heappush(q, tasks.popleft())
    return result // len(jobs)