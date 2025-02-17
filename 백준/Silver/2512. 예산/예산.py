n = int(input())
request = list(map(int, input().split()))
budget = int(input())

s = 1
e = max(request)
answer = 0

while s<=e:
    mid = (s+e)//2
    total = 0
    for r in request:
        if r<mid:
            total += r
        else:
            total += mid

    if total<=budget:
        answer = mid
        s = mid + 1
    else:
        e = mid - 1

print(answer)