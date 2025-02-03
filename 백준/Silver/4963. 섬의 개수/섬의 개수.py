import sys
input = sys.stdin.readline

dx = [0, 0, 1, -1, 1, -1, 1, -1]
dy = [1, -1, 0, 0, 1, 1, -1, -1]
def DFS(x, y):
    stack = [(x, y)]
    while stack:
        cx, cy = stack.pop()
        if graph[cx][cy] == 1:
            graph[cx][cy] = 0
            for i in range(8):
                nx = cx + dx[i]
                ny = cy + dy[i]
                if nx<0 or nx>=n or ny<0 or ny>=m:
                    continue
                elif graph[nx][ny] == 0:
                    continue
                else:
                    stack.append((nx, ny))

while True:
    m, n = map(int, input().split())
    if m == n == 0:
        break
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                DFS(i, j)
                cnt += 1
    print(cnt)