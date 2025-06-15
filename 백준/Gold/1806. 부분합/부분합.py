import sys
input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))
result = 100001

l, r = 0, 0
total = 0

while True:
    if total >= s:
        result = min(result, r-l)
        total -= nums[l]
        l += 1
    elif r == n:
        break
    else:
        total += nums[r]
        r += 1

if result == 100001:
    print(0)
else:
    print(result)