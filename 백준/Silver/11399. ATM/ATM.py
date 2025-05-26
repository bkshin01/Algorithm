import sys
input = sys.stdin.readline

n = int(input())
if n == 1:
    print(int(input()))
    exit()
    
arr = list(map(int, input().split()))
arr.sort()
result = 0
for i in range(n):
    result += arr[i]*(n-i)
print(result)