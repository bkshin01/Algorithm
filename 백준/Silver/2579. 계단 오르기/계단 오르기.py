import sys
input = sys.stdin.readline

n = int(input())
s = [0]
for _ in range(n):
    s.append(int(input()))

if n < 2:
    print(s[n])
else:
    dp = [0] * (n+1)
    dp[1] = s[1]
    dp[2] = dp[1] + s[2]

    for i in range(3, n+1):
        dp[i] = max(dp[i-2], dp[i-3]+s[i-1]) + s[i]
    print(dp[n])