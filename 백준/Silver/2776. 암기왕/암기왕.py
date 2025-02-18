import sys
input = sys.stdin.readline

def BS(sorted_arr, t):
    s, e = 0, len(sorted_arr)-1
    while s<=e:
        mid = (s+e)//2
        if sorted_arr[mid]==t:
            return 1
        elif sorted_arr[mid]<t:
            s=mid+1
        else:
            e=mid-1
    return 0

for _ in range(int(input())):
    n = int(input())
    arr1 = list(map(int, input().split()))
    m = int(input())
    arr2 = list(map(int, input().split()))
    arr1.sort()

    for test_num in arr2:
        print(BS(arr1, test_num))