def solution(n, costs):
    costs.sort(key=lambda x:x[2])
    linked = set([costs[0][0]])
    result = 0
    
    while len(linked) != n:
        for s, e, c in costs:
            if s in linked and e in linked:
                continue
            elif s in linked or e in linked:
                linked.update([s, e])
                result += c
                break
    
    return result