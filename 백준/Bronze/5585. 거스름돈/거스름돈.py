rest = 1000 - int(input())
coins = [500, 100, 50, 10, 5, 1]
result = 0

for c in coins:
    if rest == 0:
        break
    result += rest//c
    rest %= c

print(result)