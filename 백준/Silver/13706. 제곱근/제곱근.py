n = int(input())
s=1
e=n
while s<=e:
    mid = (s+e)//2
    if mid**2==n:
        print(mid)
        exit()
    elif mid**2<n:
        s=mid+1
    else:
        e=mid-1