import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

cnt = 0
s, e = 0, 1
while s <= e and e <= n:
    total = sum(nums[s:e])

    if total == m:
        cnt += 1
        s += 1
    elif total < m:
        e += 1
    else:
        s += 1

print(cnt)