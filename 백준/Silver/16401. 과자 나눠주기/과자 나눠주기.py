import sys
input = sys.stdin.readline

m, n = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
s=1
e=sum(arr)
answer = 0
while s<=e:
    mid=(s+e)//2 # 1명에게 줄 막대과자 길이
    cnt = 0
    for i in arr:
        if i>=mid:
            cnt += (i//mid)
        else:
            break
    
    if cnt<m:
        e = mid - 1
    else:
        answer = mid
        s = mid + 1

print(answer)