from collections import deque

def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5 * len(cities)
    
    result = 0
    q = deque([])
    for c in cities:
        c = c.lower()
        # cache hit
        if c in q:
            result += 1
            q.remove(c)
            q.append(c)
        # cache miss & full q
        elif len(q) == cacheSize:
            result += 5
            q.popleft()
            q.append(c)
        # cache miss & empty q
        else:
            result += 5
            q.append(c)    
            
    return result