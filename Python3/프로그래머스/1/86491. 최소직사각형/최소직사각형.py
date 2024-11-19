def solution(sizes):
    # 큰 것 중에서 가장 큰 것 * 작은 것 중에서 가장 큰 것
    x = []
    y = []
    
    for s in sizes:
        x.append(max(s))
        y.append(min(s))
    
    return max(x) * max(y)