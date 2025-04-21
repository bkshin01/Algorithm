def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    link = set([costs[0][0]]) # 연결된 섬
    
    # kruskal 알고리즘
    while len(link) != n:
        for s, e, c in costs:
            if s in link and e in link: # 이미 연결된 섬
                continue
            if s in link or e in link: # 둘 중 하나만 연결
                link.update([s, e])
                answer += c
                break
                
    return answer