import sys
input = sys.stdin.readline

n = int(input())
ropes = []
for _ in range(n):
    ropes.append(int(input()))
ropes.sort(reverse=True)

result = 0
for i in range(n):
    tmp = (i+1) * ropes[i]
    result = max(result, tmp)
print(result)