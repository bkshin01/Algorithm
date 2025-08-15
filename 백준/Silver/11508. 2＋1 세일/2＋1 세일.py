import sys
input = sys.stdin.readline

n = int(input())
prices = []
for _ in range(n):
    prices.append(int(input()))

if n <= 2:
    print(sum(prices))
else:
    prices.sort(reverse=True)
    result = 0
    for i in range(n):
        p = prices[i]
        if (i+1) % 3 == 0:
            continue
        else:
            result += p
    print(result)