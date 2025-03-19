def solution(numbers, target):
    n = len(numbers)
    h = 0
    tree = []
    tree.append([0])
    
    while h < n:
        parents = tree[h]
        tree.append([])
        nxt = tree[h+1]
        for p in parents:
            nxt.append(p+numbers[h])
            nxt.append(p-numbers[h])
        h += 1
    
    answer = 0
    for i in tree[h]:
        if i == target:
            answer += 1
                
    return answer