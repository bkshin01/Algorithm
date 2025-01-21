import sys
input = sys.stdin.readline

dx = [0, 0, 1, -1, -1, 1, -1, 1]
dy = [1, -1, 0, 0, -1, -1, 1, 1]

def DFS(gph, x, y):
    stack = [(x, y)]
    
    while stack:
        cx, cy = stack.pop()
        if gph[cx][cy] == 1:
            gph[cx][cy] = 0
            for i in range(8):
                nx = cx + dx[i]
                ny = cy + dy[i]
                if nx < 0 or nx >= h or ny < 0 or ny >= w:
                    continue
                elif gph[nx][ny] == 0:
                    continue
                else:
                    stack.append((nx, ny))

while True:
    w, h = map(int, input().split())
    if w == h == 0:
        exit()
    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))
    
    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                DFS(graph, i, j)
                cnt += 1
    print(cnt)