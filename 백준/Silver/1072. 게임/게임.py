x, y = map(int, input().split())
z = int(100*y/x)
s, e = 0, x
answer = -1

while s<=e:
    mid=(s+e)//2
    new_z = int(100*(y+mid)/(x+mid))

    if new_z>z:
        answer = mid
        e = mid-1
    else:
        s=mid+1

print(answer)