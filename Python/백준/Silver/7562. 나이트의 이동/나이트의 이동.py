import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 1, 2, 2, 1, -1, -2, -2]
dy = [2, 2, 1, -1, -2, -2, -1, 1]

def BFS(n, x, y, tx, ty):
    chess = [[0]*n for _ in range(n)]
    queue = deque()
    queue.append((x, y))

    while queue:
        cx, cy = queue.popleft()
        if cx == tx and cy == ty:
            return chess[cx][cy]
        for i in range(8):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n or chess[nx][ny]>0:
                continue
            else:
                chess[nx][ny] = chess[cx][cy] + 1
                queue.append((nx, ny))

t = int(input())
for _ in range(t):
    l = int(input())
    curr_x, curr_y = map(int, input().split())
    target_x, target_y = map(int, input().split())

    print(BFS(l, curr_x, curr_y, target_x, target_y))