def solution(numbers, target):
    arr = [numbers[0], -numbers[0]]
    
    for n in numbers[1:]:
        tmp = []
    
        for a in arr:
            tmp.append(a+n)
            tmp.append(a-n)
        arr = tmp
    
    return arr.count(target)