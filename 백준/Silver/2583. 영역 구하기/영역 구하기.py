from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def BFS(x, y):
    queue = deque()
    queue.append((x, y))
    area = 0

    while queue:
        cx, cy = queue.popleft()
        if graph[cx][cy] == 1:
            area += 1
            graph[cx][cy] = 0
            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]
                if nx<0 or nx>=n or ny<0 or ny>=m:
                    continue
                elif graph[nx][ny] == 0:
                    continue
                else:
                    queue.appendleft((nx, ny))
    return area

n, m, k = map(int, input().split())
graph = [[1] * m for _ in range(n)]

for _ in range(k):
    a, b, x, y = map(int, input().split())
    
    for i in range(a, x):
        for j in range(b, y):
            graph[j][i] = 0

result = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            result.append(BFS(i, j))

result.sort()
print(len(result))
for a in result:
    print(a, end=" ")