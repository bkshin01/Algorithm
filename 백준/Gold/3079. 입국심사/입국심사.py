import sys
input = sys.stdin.readline

n, m = map(int, input().split())
times = []
for _ in range(n):
    times.append(int(input()))

low, high = min(times), m * max(times)
result = 0

while low <= high:
    mid = (low + high) // 2
    cnt = 0

    for t in times:
        cnt += mid//t
    
    if cnt >= m:
        result = mid
        high = mid - 1
    else:
        low = mid + 1

print(result)