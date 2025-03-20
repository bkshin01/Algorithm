from heapq import heappop, heappush

def solution(n, works):
    q = []
    for w in works:
        heappush(q, -w)
        
    while n:
        cur = heappop(q)
        if cur == 0:
            return 0
        tmp = cur+1
        heappush(q, tmp)
        n -= 1
    
    answer = 0
    for i in q:
        answer += (i**2)
    
    return answer