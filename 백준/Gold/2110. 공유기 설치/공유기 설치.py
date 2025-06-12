import sys
input = sys.stdin.readline

n, c = map(int, input().split())
houses = []
for _ in range(n):
    houses.append(int(input()))
houses.sort()

l, r = 1, houses[n-1] - houses[0]
while l <= r:
    mid = (l + r) // 2
    cnt = 1
    last = houses[0]
    
    for i in range(1, n):
        if houses[i] - last >= mid:
            cnt += 1
            last = houses[i]
    
    if cnt >= c:
        result = mid
        l = mid + 1
    else:
        r = mid - 1

print(result)