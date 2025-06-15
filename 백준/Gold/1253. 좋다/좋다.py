import sys
input = sys.stdin.readline

n = int(input())
L = list(map(int, input().split()))
L.sort()
count = 0

for k in range(n):
    i = 0
    j = n - 1
    target = L[k]
    while i < j:  # 투 포인터 알고리즘
        if L[i] + L[j] == target:
            if i != k and j != k:
                count += 1
                break
            elif i == k:
                i += 1
            else:  # j == k
                j -= 1
        elif L[i] + L[j] < target:
            i += 1
        else:  # L[i] + L[j] > target:
            j -= 1

print(count)
