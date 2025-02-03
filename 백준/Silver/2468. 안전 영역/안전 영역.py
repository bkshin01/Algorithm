import copy
import sys
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def DFS(graph, x, y, r):
    stack = [(x, y)]

    while stack:
        cx, cy = stack.pop()
        if graph[cx][cy] > r:
            graph[cx][cy] = 0
            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]
                if nx<0 or nx>=n or ny<0 or ny>=n:
                    continue
                elif graph[nx][ny] <= r:
                    continue
                else:
                    stack.append((nx, ny))

n = int(input())
graph = []
m = 0
for i in range(n):
    graph.append(list(map(int, input().split())))
    if max(graph[i]) > m:
        m = max(graph[i])

result = [0] * (m+1)
for rainfall in range(m):
    cnt = 0
    tmp = copy.deepcopy(graph)
    for i in range(n):
        for j in range(n):
            if tmp[i][j] > rainfall:
                DFS(tmp, i, j, rainfall)
                cnt += 1
    result[rainfall] = cnt

print(max(result))