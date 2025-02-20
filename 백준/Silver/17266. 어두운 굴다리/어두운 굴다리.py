import sys
input = sys.stdin.readline

def is_possible(arr, height):
    if height - arr[0] < 0:
        return False
    
    for i in range(1, m):
        if arr[i]-arr[i-1] > 2*height:
            return False
    
    if n-arr[-1] > height:
        return False
    
    return True

n = int(input())
m = int(input())
x = list(map(int, input().split()))

s = 1
e = n
answer = n

while s<=e:
    mid = (s+e)//2
    if is_possible(x, mid):
        answer = mid
        e = mid - 1
    else:
        s = mid + 1

print(answer)