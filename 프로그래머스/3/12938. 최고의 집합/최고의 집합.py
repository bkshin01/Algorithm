def solution(n, s):
    if n > s:
        return [-1]
    
    if s % n == 0:
        return [s//n]*n
    else:
        tmp = [s//n]*n
        for i in range(s%n):
            tmp[i] += 1
        return sorted(tmp)