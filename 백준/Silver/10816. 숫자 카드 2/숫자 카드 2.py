import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
cards = {}
for i in arr:
    if i in cards:
        cards[i]+=1
    else:
        cards[i]=1
        
m = int(input())
target = list(map(int, input().split()))
result = []
for t in target:
    if t in cards:
        result.append(cards[t])
    else:
        result.append(0)

print(*result)