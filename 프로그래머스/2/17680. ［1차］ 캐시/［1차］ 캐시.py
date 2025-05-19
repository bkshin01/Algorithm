from collections import deque

def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5 * len(cities)
    
    result = 0
    q = deque([])
    for c in cities:
        c = c.lower()
        if c in q:
            result += 1
            q.remove(c)
            q.append(c)
        elif len(q) == cacheSize:
            result += 5
            q.popleft()
            q.append(c)
        else:
            result += 5
            q.append(c)    
            
    return result