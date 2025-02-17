import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

cards.sort()

def BS(sorted_arr, t):
    s, e = 0, len(sorted_arr)-1
    while s<=e:
        mid = (s+e)//2
        if sorted_arr[mid]==t:
            return 1
        elif sorted_arr[mid]<t:
            s = mid + 1
        else:
            e = mid - 1
    return 0

for t in targets:
    print(BS(cards, t), end=" ")