from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def BFS(queue):
    while queue:
        for _ in range(len(queue)):
            cx, cy = queue.popleft()
            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]
                if nx<0 or nx>=n or ny<0 or ny>=m:
                    continue
                elif graph[nx][ny] != 0:
                    continue
                else:
                    graph[nx][ny] = graph[cx][cy] + 1
                    queue.append((nx, ny))

m, n = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

queue = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i, j))

BFS(queue)

day = 0
for line in graph:
    for tomato in line:
        if tomato == 0:
            print(-1)
            exit()
    day = max(day, max(line))
print(day - 1)