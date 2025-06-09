import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []

for _ in range(n):
    coins.append(int(input()))
coins.sort(reverse=True)

idx = 0
result = 0
while k:
    result += k//coins[idx]
    k %= coins[idx]
    idx += 1

print(result)