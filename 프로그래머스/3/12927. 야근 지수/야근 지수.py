from heapq import heappop, heappush

def solution(n, works):
    result = 0
    arr = []
    
    for w in works:
        heappush(arr, -w)
    
    while n:
        cur = -heappop(arr)
        if cur == 0:
            return 0
        else:
            cur -= 1
            heappush(arr, -cur)
            n -= 1
    
    for a in arr:
        result += (a**2)
        
    return result