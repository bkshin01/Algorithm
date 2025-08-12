import sys
input = sys.stdin.readline

n = int(input())
people = []
for _ in range(n):
    x, y = map(int, input().split())
    people.append((x, y))

ranks = []
for i in range(n):
    cx, cy = people[i]
    cnt = 0
    for j in range(n):
        if i != j:
            tx, ty = people[j]
            if cx < tx and cy < ty:
                cnt += 1
    ranks.append(cnt+1)

print(*ranks)