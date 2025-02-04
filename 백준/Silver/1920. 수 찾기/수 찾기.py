import sys
input = sys.stdin.readline

def binSearch(arr, t):
    s = 0
    e = n-1
    while s <= e:
        mid = (s + e) // 2
        if arr[mid] == t:
            return 1
        elif arr[mid] > t:
            e = mid-1
        else:
            s = mid+1
    return 0

n = int(input())
array = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

array.sort()
for t in targets:
    print(binSearch(array, t))