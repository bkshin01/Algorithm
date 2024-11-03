def solution(clothes):
    closet = {}
    for info in clothes:
        key, value = info[1], info[0]
        if key in closet.keys():
            closet[key] += [value]
        else:
            closet[key] = [value]
    
    answer = 1
    for key, value in closet.items():
        answer *= (len(value) + 1)
    
    return answer - 1