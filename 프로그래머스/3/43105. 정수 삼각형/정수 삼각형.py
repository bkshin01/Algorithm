def solution(triangle):
    n = len(triangle)
    if n == 1:
        return triangle[0][0]
    
    dp = [[0] * (i+1) for i in range(n)]
    dp[0][0] = triangle[0][0]
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + triangle[i][0]
        dp[i][i] = dp[i-1][i-1] + triangle[i][i]
    
    for i in range(2, n):
        for j in range(1, i):
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])+triangle[i][j]
    
    return max(dp[n-1])