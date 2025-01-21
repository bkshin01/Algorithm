import sys
import copy
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def DFS(graph, x, y, r):
    visited = []
    stack = [(x, y)]
    
    while stack:
        cx, cy = stack.pop()
        if (cx, cy) not in visited:
            visited.append((cx, cy))
            graph[cx][cy] = 0
            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                elif tmp[nx][ny] <= r:
                    continue
                else:
                    DFS(graph, nx, ny, r)

n = int(input())
org_graph = []
MAX = 0
for i in range(n):
    org_graph.append(list(map(int, input().split())))
    if max(org_graph[i]) > MAX:
        MAX = max(org_graph[i])

rain_cnt = []
for r in range(1, MAX):
    rainfall = r
    cnt = 0
    tmp = copy.deepcopy(org_graph)
    for i in range(n):
        for j in range(n):
            if tmp[i][j] > r:
                DFS(tmp, i, j, rainfall)
                cnt += 1
    rain_cnt.append(cnt)
if len(rain_cnt) > 0:
    print(max(rain_cnt))
else:
    print(1)