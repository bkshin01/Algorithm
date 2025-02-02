import sys
input = sys.stdin.readline

def DP(n, sticker):
    dp = [[0] * n for _ in range(2)]
    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]

    for j in range(1, n):
        for i in range(2):
            dp[i][j] = max(dp[i][j-1], dp[1-i][j-1] + sticker[i][j])

    # DEBUGGING
    # print("")
    # for i in dp:
    #     print(i)

    return max(dp[0][n-1], dp[1][n-1])

for _ in range(int(input())):
    n = int(input())
    line_1 = list(map(int, input().split()))
    line_2 = list(map(int, input().split()))
    full_sticker = [line_1, line_2]
    print(DP(n, full_sticker))