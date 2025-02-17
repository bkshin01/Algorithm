import sys
input = sys.stdin.readline

k, n = map(int, input().split())
length = [int(input()) for _ in range(k)]
s=1
e=max(length)

while s<=e:
    mid = (s+e)//2
    total = 0
    for l in length:
        total += (l//mid)
    
    if total >= n:
        s = mid+1
    else:
        e = mid-1
    
print(e)