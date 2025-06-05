def solution(triangle):
    n = len(triangle)
    dp = [[0] * i for i in range(1, n+1)]
    dp[0][0] = triangle[0][0]
    
    for i in range(1, n):
        for j in range(i+1):
            dp[i][j] = triangle[i][j]
            if j == 0:
                dp[i][j] += dp[i-1][0]
            elif j == i:
                dp[i][j] += dp[i-1][j-1]
            else:
                dp[i][j] += max(dp[i-1][j], dp[i-1][j-1])
                
    return max(dp[n-1])