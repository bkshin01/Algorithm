def to_next(x):
    if x % 2 == 1:
        x = (x+1)//2
    else:
        x = x//2
    return x

def solution(n,a,b):
    result = 1
    while True:
        if abs(a-b)==1 and max(a, b)%2==0:
            return result
        
        a = to_next(a)
        b = to_next(b)
        result += 1