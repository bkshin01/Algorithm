def solution(elements):
    all_num = set()
    all_num.update(elements)
    n = len(elements)
    
    for i in range(2, n+1):
        tmp = sum(elements[:i])
        all_num.add(tmp)
        
        for j in range(n-1):
            tmp -= elements[j]
            if j+i < n:
                tmp += elements[j+i]
            else:
                tmp += elements[j+i-n]
            all_num.add(tmp)
            
    return len(all_num)