import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = list(map(int, input().split()))
s=1
e=max(tree)

while s<=e:
    log = 0
    mid = (s+e)//2
    for t in tree:
        if t>mid:
            log += (t-mid)
    
    if log >= m:
        s = mid+1
    else:
        e = mid-1

print(e)