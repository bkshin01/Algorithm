def solution(n, lost, reserve):
    r_set = set(reserve) - set(lost)
    l_set = set(lost) - set(reserve)
    
    for r in r_set:
        if r-1 in l_set:
            l_set.remove(r-1)
        elif r+1 in l_set:
            l_set.remove(r+1)
    
    return n - len(l_set)