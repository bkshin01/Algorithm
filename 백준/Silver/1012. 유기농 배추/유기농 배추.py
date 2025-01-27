dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def DFS(x, y):
    stack = [(x, y)]

    while stack:
        cx, cy = stack.pop()
        if graph[cx][cy] == 1:
            graph[cx][cy] = 0
            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]
                if nx<0 or nx>=n or ny<0 or ny>=m:
                    continue
                elif graph[nx][ny] == 0:
                    continue
                else:
                    stack.append((nx, ny))

for _ in range(int(input())):
    m, n, k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    
    # DEBUGGING
    # for i in graph:
    #     print(i)

    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                DFS(i, j)
                cnt += 1

    print(cnt)