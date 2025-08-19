import sys
input = sys.stdin.readline

n = int(input())
liquids = list(map(int, input().split()))
liquids.sort()

result = [0, 0, 2000000000]
start, end = 0, n-1
while start < end:
    s, e = liquids[start], liquids[end]
    tmp = s+e
    if abs(tmp) < result[2]:
        result = [s, e, abs(tmp)]
    elif s+e>0:
        end -= 1
    else:
        start += 1

print(*result[:2])