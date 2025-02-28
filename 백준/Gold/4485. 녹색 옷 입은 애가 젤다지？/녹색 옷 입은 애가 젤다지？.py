import sys
from heapq import heappop, heappush
input = sys.stdin.readline
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

cnt = 0
while True:
    n = int(input())
    if n == 0:
        exit()
    cnt += 1
    
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    queue = []
    distance = [[float("inf")] * n for _ in range(n)]
    distance[0][0] = arr[0][0]
    heappush(queue, (arr[0][0], 0, 0))

    while queue:
        dist, cy, cx = heappop(queue)
        if cx ==  n-1 and cy == n-1:
            print(f"Problem {cnt}: {dist}")
            break
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                cost = dist + arr[ny][nx]
                if distance[ny][nx] > cost:
                    distance[ny][nx] = dist + arr[ny][nx]
                    heappush(queue, (dist + arr[ny][nx], ny, nx))