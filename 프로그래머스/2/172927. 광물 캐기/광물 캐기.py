def solution(picks, minerals):
    total = sum(picks)
    if len(minerals) > total * 5:
        minerals = minerals[:total*5]
    
    n = len(minerals)
    new_minerals = [[0, 0, 0] for _ in range((n//5)+1)]

    for i in range(n):
        m = minerals[i]
        if m == 'diamond':
            new_minerals[i//5][0] += 25
        elif m == 'iron':
            new_minerals[i//5][1] += 5
        else:
            new_minerals[i//5][2] += 1
    
    result = 0
    new_minerals.sort()
    while picks and new_minerals:
        d, i, s = new_minerals.pop()
        if picks[0] > 0:
            result += (d//25 + i//5 + s)
            picks[0] -= 1
        elif picks[1] > 0:
            result += (d//5 + i//5 + s)
            picks[1] -= 1
        else:
            result += (d + i + s)
            picks[2] -= 1
    
    return result