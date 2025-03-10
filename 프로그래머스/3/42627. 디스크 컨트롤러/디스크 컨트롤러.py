from heapq import heappop, heappush

def solution(jobs):
    answer = 0
    time = 0
    n = 0  
    start = -1
    q = []
    
    while n < len(jobs):
        for j in jobs:
            if start < j[0] <= time:
                heappush(q, (j[1], j[0]))

        if q:
            cur = heappop(q)
            start = time
            time += cur[0]
            answer += time - cur[1]
            n += 1
        else:
            time += 1
            
    return answer // len(jobs)