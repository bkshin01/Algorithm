def solution(n, times):
    l, r = 1, max(times) * n
    while l <= r:
        mid = (l+r) // 2
        done_people = 0
        
        for t in times:
            done_people += mid // t
            if done_people >= n:
                break
        
        if done_people >= n:
            answer = mid
            r = mid - 1
        else:
            l = mid + 1
            
    return answer