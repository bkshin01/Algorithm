def GCD(x, y):
    candidate = []
    for i in range(1, x+1):
        if x%i==0:
            candidate.append(i)
    result = 0
    for c in candidate:
        if y%c==0 and c>result:
            result = c
    return result

def solution(a, b):
    x = b // GCD(a, b)
    arr = []
    for i in range(2, x+1):
        if x%i==0:
            arr.append(i)
    for a in arr:
        if a % 2 == 0 or a % 5 == 0:
            pass
        else:
            return 2
    return 1