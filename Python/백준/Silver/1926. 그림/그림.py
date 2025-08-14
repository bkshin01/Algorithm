import sys
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def DFS(x, y):
    stack = [(x, y)]
    graph[x][y] = 0
    area = 0

    while stack:
        cx, cy = stack.pop()
        area += 1
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            elif graph[nx][ny] == 0:
                continue
            else:
                stack.append((nx, ny))
                graph[nx][ny] = 0
    return area
        

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

result = [0]
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            result.append(DFS(i, j))

result.sort(reverse=True)
print(len(result)-1)
print(result[0])