from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
maps = [-1] * (101)
maps[1] = 0

ladders = {}
for _ in range(n):
    s, e = map(int, input().split())
    ladders[s] = e

snakes = {}
for _ in range(m):
    s, e = map(int, input().split())
    snakes[s] = e

# 너비 우선 탐색
q = deque([1])

while q:
    cur = q.popleft()

    for i in range(1, 7):
        nxt = cur + i
        if nxt > 100:
            continue

        if nxt in ladders:
            nxt = ladders[nxt]
        elif nxt in snakes:
            nxt = snakes[nxt]
        
        if maps[nxt] == -1:
            maps[nxt] = maps[cur] + 1
            q.append(nxt)
        
        if nxt == 100:
            print(maps[nxt])
            exit()