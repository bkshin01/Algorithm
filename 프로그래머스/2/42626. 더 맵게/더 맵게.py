from heapq import heappush, heappop

def solution(scoville, K):
    answer = 0
    q = []
    for s in scoville:
        heappush(q, s)
    
    while len(q) > 1:
        front = heappop(q)
        if front >= K:
            return answer
        else:
            new_s = front + (heappop(q) * 2)
            heappush(q, new_s)
            answer += 1
    
    front = heappop(q)
    if front >= K:
        return answer
    else:
        return -1