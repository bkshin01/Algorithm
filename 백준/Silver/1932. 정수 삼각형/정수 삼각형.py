n = int(input())
triangle = []
for _ in range(n):
    triangle.append(list(map(int, input().split())))

# DEBUGGING
# print(triangle)

dp = []
for i in range(n):
    dp.append([0]*(i+1))
dp[0][0] = triangle[0][0]

if n == 1:
    print(triangle[0][0])
    exit()

dp[1][0] = dp[0][0] + triangle[1][0]
dp[1][1] = dp[0][0] + triangle[1][1]

# DEBUGGING
# for i in range(len(dp)):
#     print(dp[i])

for i in range(2, n):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = dp[i-1][j] + triangle[i][j]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + triangle[i][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]

# DEBUGGING
# for i in range(len(dp)):
#     print(dp[i])

print(max(dp[n-1]))