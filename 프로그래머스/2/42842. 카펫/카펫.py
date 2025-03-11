def solution(brown, yellow):
    arr = []
    for i in range(1, int(yellow**0.5)+1):
        if yellow%i==0:
            arr.append((i, yellow//i))
    
    answer = []
    for candidate in arr:
        a, b = candidate[0], candidate[1]
        if (a+2)*(b+2)-yellow==brown:
            answer.append(a+2)
            answer.append(b+2)
    
    return sorted(answer, reverse=True)