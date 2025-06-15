import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
nums.sort()
x = int(input())

cnt = 0
l, r = 0, n-1
while l < r:
    sum = nums[l] + nums[r]
    if sum == x:
        cnt += 1
        l += 1
        r -= 1
    elif sum < x:
        l += 1
    else:
        r -= 1

print(cnt)