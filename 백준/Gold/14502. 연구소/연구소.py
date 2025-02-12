from collections import deque
import copy
import sys
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def BFS():
    queue = deque()
    tmp = copy.deepcopy(graph)

    # 바이러스 큐에 추가
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 2:
                queue.append((i, j))
    
    # 큐에 있는 바이러스로 감염 진행
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if tmp[nx][ny] == 0:
                tmp[nx][ny] = 2
                queue.append((nx, ny))
    
    # 안전영역 계산
    global answer
    cnt = 0

    for i in range(n):
        cnt += tmp[i].count(0)
    
    answer = max(answer, cnt)

def make_wall(cnt):
    if cnt == 3:
        BFS()
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                make_wall(cnt+1)
                graph[i][j] = 0

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

answer = 0
make_wall(0)

print(answer)