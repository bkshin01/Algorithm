import sys
input = sys.stdin.readline

n = int(input())
ropes = []
for i in range(n):
    ropes.append(int(input()))

if n == 1:
    print(ropes[0])
else:
    ropes.sort(reverse=True)
    result = 0
    for i in range(n):
        r = ropes[i]
        result = max(result, r*(i+1))
    print(result)