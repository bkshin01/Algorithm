import sys
input = sys.stdin.readline

weights = [int(input()) for _ in range(9)]
weights.sort()

target = sum(weights) - 100
s, e = 0, len(weights)-1 # 8

while s < e:
    tmp = weights[s] + weights[e]
    if tmp > target:
        e -= 1
    elif tmp < target:
        s += 1
    else:
        for i in range(9):
            if i != s and i != e:
                print(weights[i])
        break