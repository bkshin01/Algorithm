MOD = 1000000007

def solution(n):
    dp = [0 for _ in range(n+1)]
    dp[1] = 1
    dp[2] = 2
    if n <= 2:
        return dp[n]
    
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % MOD
    
    return dp[n]