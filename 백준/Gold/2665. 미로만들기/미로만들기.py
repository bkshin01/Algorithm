# 미로 탐색과 유사. 가중치는 방을 바꾼 횟수
from collections import deque
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    queue = deque()
    queue.append((0, 0))
    visited = [[-1] * n for _ in range(n)]
    visited[0][0] = 0
    
    while queue:
        cx, cy = queue.popleft()
        if cx == n-1 and cy == n-1:
            return visited[cx][cy]
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                if graph[nx][ny] == 1: # 문제 없이 이동하는 경우
                    queue.appendleft((nx, ny))
                    visited[nx][ny] = visited[cx][cy]
                else: # 방을 바꿔야 하는 경우
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[cx][cy] + 1

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

print(bfs())