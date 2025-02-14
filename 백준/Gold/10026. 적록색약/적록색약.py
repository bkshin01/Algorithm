from collections import deque
import sys
sys.setrecursionlimit(1000000)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def DFS(x, y):
    visited[x][y] = True
    cur_color = graph[x][y]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=n:
            continue
        elif visited[nx][ny] == False:
            if graph[nx][ny] == cur_color:
                DFS(nx, ny)

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(input()))
three_cnt, two_cnt = 0, 0

visited = [[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j]==False:
            DFS(i, j)
            three_cnt+=1

for i in range(n):
    for j in range(n):
        if graph[i][j]=='R':
            graph[i][j]='G'

visited = [[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j]==False:
            DFS(i, j)
            two_cnt+=1

print(three_cnt, two_cnt)