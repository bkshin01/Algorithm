import sys
input = sys.stdin.readline

def BS(arr, target):
    s=0
    e=len(arr)-1
    while s<=e:
        mid=(s+e)//2
        if arr[mid]==target:
            return True
        elif arr[mid]>target:
            e=mid-1
        else:
            s=mid+1
    return False

while True:
    n, m = map(int, input().split())
    if n==m==0:
        exit()
    sg=[]
    cnt = 0
    for _ in range(n):
        sg.append(int(input()))
    for _ in range(m):
        target = int(input())
        if BS(sg, target):
            cnt += 1
    print(cnt)