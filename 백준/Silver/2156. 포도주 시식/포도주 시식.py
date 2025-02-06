n = int(input())
wine = [0]
for _ in range(n):
    wine.append(int(input()))
dp = [0]*(n+1)
dp[1] = wine[1]

if n == 1:
    print(wine[1])
elif n == 2:
    dp[2] = wine[1] + wine[2]
    print(dp[2])
else:
    dp[2] = wine[1] + wine[2]
    for i in range(3, n+1):
        dp[i] = max(dp[i-1], wine[i]+dp[i-2], wine[i]+wine[i-1]+dp[i-3])
    print(dp[n])