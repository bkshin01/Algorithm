n = int(input())
arr = list(map(int, input().split()))
dp = [1] * (n) 
# dp[i]는 i번째 숫자를 마지막으로 하는 부분배열 중 가장 긴 감소하는 부분배열의 길이

for i in range(n):
    for j in range(i):
        if arr[i]<arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))