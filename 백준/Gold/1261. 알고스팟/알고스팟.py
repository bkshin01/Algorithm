# 미로탐색과 유사. 가중치는 벽을 부순 횟수
# 가중치가 0이면 appendleft, 1이면 append
from collections import deque
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

m, n = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input())))
distance = [[-1]*m for _ in range(n)] # 가중치

queue = deque()
queue.append((0, 0))
distance[0][0] = 0
while queue:
    cx, cy = queue.popleft()
    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if distance[nx][ny] == -1:
                if arr[nx][ny] == 0:
                    distance[nx][ny] = distance[cx][cy]
                    queue.appendleft((nx, ny))
                else:
                    distance[nx][ny] = distance[cx][cy] + 1
                    queue.append((nx, ny))
    
print(distance[n-1][m-1])