def solution(n, lost, reserve):
    l_set = set(lost)
    r_set = set(reserve)
    lost = l_set-r_set
    reserve = r_set-l_set
    
    save = []
    for l in lost:
        if l-1 in reserve:
            save.append(l)
            reserve.remove(l-1)
        elif l+1 in reserve:
            save.append(l)
            reserve.remove(l+1)
    return n-len(lost)+len(save)