MAX = 5000
def dp(target):
    # 메모이제이션
    dp = [-1] * (MAX + 1)
    dp[3] = 1
    dp[5] = 1

    # 점화식
    for i in range(6, target+1):
        if i % 5 == 0:
            dp[i] = dp[i-5] + 1
        elif i % 3 == 0:
            dp[i] = dp[i-3] + 1
        elif dp[i-3] > 0 and dp[i-5] > 0:
            dp[i] = min(dp[i-3], dp[i-5]) + 1
    return dp[target]

n = int(input())
print(dp(n))