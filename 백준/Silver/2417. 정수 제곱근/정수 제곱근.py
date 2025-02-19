n = int(input())
s=0
e=n
answer = 0
while s<=e:
    mid=(s+e)//2
    if mid**2>=n:
        answer = mid
        e = mid - 1
    else:
        s = mid + 1
print(answer)