import sys
input = sys.stdin.readline

time = []
n = int(input())
for _ in range(n):
    s, e = map(int, input().split())
    time.append([s, e])

time.sort(key=lambda x:(x[1], x[0]))
last_end = time[0][1]
result = 1

for i in range(1, n):
    if time[i][0] >= last_end:
        last_end = time[i][1]
        result += 1

print(result)