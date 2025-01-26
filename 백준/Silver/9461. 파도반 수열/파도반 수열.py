import sys
input = sys.stdin.readline

def dp(n):
    p = [1 for _ in range(n+1)]

    for i in range(3, n+1):
        p[i] = p[i-3] + p[i-2]
    
    return p[n-1]

for _ in range(int(input())):
    print(dp(int(input())))