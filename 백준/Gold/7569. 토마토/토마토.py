from collections import deque
import sys
input = sys.stdin.readline

m, n, h = map(int, input().split())
matrix = [[] for _ in range(h)]
for i in range(h):
    for _ in range(n):
        matrix[i].append(list(map(int, input().split())))

tomatos = deque()
for i in range(h): # 각 층마다
    for j in range(n): # 각 줄마다
        for k in range(m):
            if matrix[i][j][k] == 1:
                tomatos.append((i, j, k, 0))

days = 0
dz = [1, -1, 0, 0, 0, 0]
dx = [0, 0, 1, -1, 0, 0]
dy = [0, 0, 0, 0, -1, 1]
while tomatos:
    cz, cx, cy, cd = tomatos.popleft()
    days = max(days, cd)
    if matrix[cz][cx][cy] == 1:
        for i in range(6):
            nz = cz + dz[i]
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0<=nz<h and 0<=nx<n and 0<=ny<m:
                if matrix[nz][nx][ny] == 0:
                    matrix[nz][nx][ny] = 1
                    tomatos.append((nz, nx, ny, cd+1))

for i in range(h): # 각 층마다
    for j in range(n): # 각 줄마다
        for k in range(m):
            if matrix[i][j][k] == 0:
                print(-1)
                exit()

print(days)