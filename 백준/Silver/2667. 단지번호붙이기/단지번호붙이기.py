from collections import deque

def BFS(x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0
    cnt = 1
    
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            elif graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                cnt += 1

    return cnt

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
cnt = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt.append(BFS(i, j))
            
cnt.sort()
print(len(cnt))
for c in cnt:
    print(c)