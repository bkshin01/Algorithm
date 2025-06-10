import sys
input = sys.stdin.readline

n = int(input())
a_arr = sorted(list(map(int, input().split())))
b_arr = sorted(list(map(int, input().split())), reverse=True)

result = 0
for i in range(n):
    result += a_arr[i]*b_arr[i]
print(result)