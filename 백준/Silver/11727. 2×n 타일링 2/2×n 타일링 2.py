MAX = 10 ** 3
MOD = 10007

n = int(input())
dp = [0] * (MAX + 1)
dp[1] = 1
dp[2] = 3

for i in range(3, n+1):
    dp[i] = dp[i-2] * 2 + dp[i-1]
    
print(dp[n]%MOD)