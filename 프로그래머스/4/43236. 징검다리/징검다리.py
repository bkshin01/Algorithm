def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    low, high = 1, distance
    
    while low <= high:
        mid = (low + high) // 2
        cnt = 0
        last = 0
        
        for r in rocks:
            if r - last < mid:
                cnt += 1
                if cnt > n:
                    break
            else:
                last = r
        
        if cnt > n:
            high = mid - 1
        else:
            result = mid
            low = mid + 1
    
    return result