import sys
input = sys.stdin.readline

n = int(input())
if n == 1:
    print(0)
    exit()

arr = [True] * (n+1)
arr[0], arr[1] = False, False

# 에라토스테네스의 채
for i in range(2, int(n**0.5)+1):
    if arr[i]:
        for j in range(i*i, n+1, i):
            arr[j] = False

primes = [i for i in range(2, n+1) if arr[i]]

s, e = 0, 0
cnt = 0
while e <= len(primes):
    total = sum(primes[s:e])
    if total == n:
        cnt += 1
        e += 1
    elif total < n:
        e += 1
    else:
        s += 1

print(cnt)