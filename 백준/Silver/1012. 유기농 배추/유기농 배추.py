dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def BFS(x, y):
    queue = [(x, y)]
    while queue:
        cx, cy = queue.pop()
        if graph[cx][cy] == 1:
            graph[cx][cy] = 0
            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]
                if nx<0 or nx>=m or ny<0 or ny>=n:
                    continue
                elif graph[nx][ny] == 1:
                    queue.append((nx, ny))

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * n for _ in range(m)]
    
    for _ in range(k):
        a, b = map(int, input().split())
        graph[a][b] = 1
    
    count = 0
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                BFS(i, j)
                count += 1

    print(count)