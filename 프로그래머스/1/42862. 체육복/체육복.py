def solution(n, lost, reserve):
    r_list = list((set(reserve) - set(lost)))
    l_list = list((set(lost) - set(reserve)))
    
    for r in r_list:
        if r-1 in l_list:
            l_list.remove(r-1)
        elif r+1 in l_list:
            l_list.remove(r+1)
            
    return n-len(l_list)