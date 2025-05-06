def solution(n, lost, reserve):
    l_set = set(lost)
    r_set = set(reserve)
    
    lost = sorted(l_set-r_set)
    reserve = sorted(r_set-l_set)
    
    for l in lost[:]:
        if l - 1 in reserve:
            lost.remove(l)
            reserve.remove(l - 1)
        elif l+1 in reserve:
            lost.remove(l)
            reserve.remove(l + 1)
            
    return n - len(lost)