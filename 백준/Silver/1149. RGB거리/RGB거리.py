import sys
input = sys.stdin.readline

n = int(input())
rgb = [[0, 0, 0]]
for _ in range(n):
    rgb.append(list(map(int, input().split())))

dp = [[0, 0, 0] for _ in range(n+1)]
dp[1] = rgb[1]

for i in range(2, n+1):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + rgb[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + rgb[i][1]
    dp[i][2] = min(dp[i-1][1], dp[i-1][0]) + rgb[i][2]

print(min(dp[n]))