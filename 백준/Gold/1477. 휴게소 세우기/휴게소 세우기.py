import sys
input = sys.stdin.readline

n, m, l = map(int, input().split())
rests = list(map(int, input().split()))
rests.append(0)
rests.append(l)
rests.sort()

low, high = 1, l-1
result = 0

while low <= high:
    mid = (low + high) // 2
    cnt = 0
    for i in range(1, len(rests)):
        if rests[i] - rests[i-1] > mid:
            cnt += (rests[i] - rests[i-1] - 1) // mid
    
    if cnt > m:
        low = mid + 1
    else:
        result = mid
        high = mid - 1

print(result)