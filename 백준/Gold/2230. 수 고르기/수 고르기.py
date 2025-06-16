import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = []
for _ in range(n):
    nums.append(int(input()))
nums.sort()

diff = 2 * 10**9
l, r = 0, 0

while l <= r and r < n:
    tmp = nums[r] - nums[l]

    if tmp == m:
        print(m)
        exit()

    elif tmp < m:
        r += 1

    else:
        diff = min(diff, tmp)
        l += 1

print(diff)