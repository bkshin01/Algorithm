def solution(n, s):
    if s < 2 or n > s:
        return [-1]
    
    a = s // n
    b = s % n
    result = [a for _ in range(n)]
    
    for i in range(n):
        if i >= n - b:
            result[i] += 1
    
    return result