import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lectures = list(map(int, input().split()))

result = 0
low, high = max(lectures), sum(lectures)

while low <= high:
    mid = (low + high) // 2
    cnt = 1
    total = 0
    
    for l in lectures:
        if total + l > mid:
            cnt += 1
            total = 0
        total += l
    
    if cnt <= m:
        result = mid
        high = mid - 1
    else:
        low = mid + 1

print(result)