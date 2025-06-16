import sys
input = sys.stdin.readline

n = int(input())
liquids = list(map(int, input().split()))

result = [abs(liquids[0] + liquids[n-1]), liquids[0], liquids[n-1]]
l, r = 0, n-1
while l < r:
    tmp = liquids[l] + liquids[r]
    if abs(tmp) < result[0]:
        result[0] = abs(tmp)
        result[1], result[2] = liquids[l], liquids[r]
    
    if tmp == 0:
        break
    elif tmp > 0:
        r -= 1
    else:
        l += 1

print(*result[1:])