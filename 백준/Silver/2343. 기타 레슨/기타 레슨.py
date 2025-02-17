import sys
input = sys.stdin.readline

n, m = map(int, input().split())
time = list(map(int, input().split()))
s=max(time)
e=sum(time)

while s<=e:
    mid = (s+e)//2
    total = 0
    cnt = 1
    for t in time:
        if total + t > mid:
            cnt += 1
            total = 0
        total += t
    
    if cnt <= m:
        answer = mid
        e = mid-1
    else:
        s = mid+1
        
print(answer)