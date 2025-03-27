def solution(stones, k):
    l, r = 1, 200000000
    while l <= r:
        tmp = stones.copy()
        mid = (l+r) // 2
        cnt = 0
        for t in tmp:
            if t - mid <= 0:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                break
        if cnt >= k:
            r = mid - 1
        else:
            l = mid + 1
        
    return l