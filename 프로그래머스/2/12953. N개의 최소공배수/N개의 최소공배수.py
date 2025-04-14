def GCD(a, b):
    candidate = []
    for i in range(1, a+1):
        if a%i==0:
            candidate.append(i)
    result = 0
    for c in candidate:
        if b%c==0 and c>result:
            result = c
    return result

def solution(arr):
    LCM = arr[0]
    for num in arr:
        LCM = LCM*num // GCD(LCM, num)
    return LCM