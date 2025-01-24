from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def BFS(graph):
    queue = deque()
    queue.append((0, 0))

    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            elif graph[nx][ny] == 0:
                continue
            elif graph[nx][ny] == 1:
                graph[nx][ny] = graph[cx][cy] + 1
                queue.append((nx, ny))
    return graph[n-1][m-1]

n, m = map(int, input().split())
maze = []
for _ in range(n):
    maze.append(list(map(int, input())))

print(BFS(maze))