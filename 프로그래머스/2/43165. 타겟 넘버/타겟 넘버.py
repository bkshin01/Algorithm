def solution(numbers, target):
    leaves = [[] for _ in range(len(numbers))]
    leaves[0] = [numbers[0], -numbers[0]]
    
    for i in range(len(numbers)-1):
        parents = leaves[i]
        for p in parents:
            leaves[i+1].append(p+numbers[i+1])
            leaves[i+1].append(p-numbers[i+1])

    answer = 0
    for l in leaves[-1]:
        if l == target:
            answer += 1
    return answer