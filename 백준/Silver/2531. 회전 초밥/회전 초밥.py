import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
sushi = []
for _ in range(n):
    sushi.append(int(input()))

sushi += sushi[:k-1]
result = 0
s = 0

while s < n:
    window = set(sushi[s:s+k] + [c])
    result = max(result, len(window))
    s += 1

print(result)