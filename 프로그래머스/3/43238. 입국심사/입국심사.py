def solution(n, times):
    s, e = 1, max(times) * n
    while s <= e:
        mid = (s + e) // 2
        complete = 0
        
        for t in times:
            complete += mid // t
            if complete >= n:
                break
                
        if complete >= n:
            result = mid
            e = mid - 1
        else:
            s = mid + 1
            
    return result